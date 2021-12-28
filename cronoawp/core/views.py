from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib import messages
import io

from cronoawp.core.relatorio import criar_planilha, gerar_cronograma


def home(request):
    return render(request,'index.html')


class ExportarExcel(View):
    def get(self,  request):

        output = io.BytesIO()

        criar_planilha(output)

        output.seek(0)

        filename = 'awp_management.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response


def ImportatExcel(request):
    if request.method == 'POST':
        nova_planilha = File(request.FILES['excel_file'])
        if not nova_planilha.name.endswith('xlsx'):
            print('arquivo não permitido')
            messages.info(request, 'Formato de arquivo incompativel! Só é aceito arquivo .xlsx')
            return render(request, 'index.html')


        output = io.BytesIO()

        gerar_cronograma(nova_planilha,output)

        output.seek(0)

        filename = 'awp.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response

    return render(request, 'index.html')


