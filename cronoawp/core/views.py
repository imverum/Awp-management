from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib import messages
import io

from cronoawp.core.relatorio import criar_planilha, gerar_cronograma
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def ImportatExcel(request):
    if request.method == 'POST':
        nova_planilha = File(request.FILES['excel_file'])
        if not nova_planilha.name.endswith('xlsx'):
            print('arquivo não permitido')
            messages.error(request, 'Formato de arquivo incompativel! Só é aceito arquivo .xlsx')
            return render(request, 'index.html')


        output = io.BytesIO()
        e = ""
        try:
            gerar_cronograma(nova_planilha,output)
        except ValueError as e:
            if "not found" in str(e):
                erro = "Verifique o nomes das abas de sua planilha!  wp_type, standard_activities, cwa, wp e general"
                messages.error(request, erro)

                list(messages.get_messages(request))
                return render(request, 'index.html')

        output.seek(0)

        filename = 'awp.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response

    return render(request, 'index.html')




