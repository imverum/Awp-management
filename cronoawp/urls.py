from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cronoawp.core.views import home, ExportarExcel, ImportatExcel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ImportatExcel, name='import_excel'),
    path('',home,name='home'),
    path('', include('cronoawp.account.urls')),
    path('exportarexcel',ExportarExcel, name='exportar_excel'),
]
