from django.contrib import admin

from cronoawp.core.models import Wp_type, Standard_activities


class Wp_typeModelAdmin(admin.ModelAdmin):
    list_display = ('sub_discipline', 'discipline','sub_discipline_id')
    search_fields = ('sub_discipline', 'discipline','sub_discipline_id')
    list_filter = ('discipline',)

class Standard_activitiesModelAdmin(admin.ModelAdmin):
    list_display = ('sub_discipline', 'work_package_type','project_phase', 'discipline', 'activity_name', 'standard_activities_id',
                    'predecessor', 'relation', 'lag', 'duration', 'physical_progress', 'financial_progress', 'responsible')

    search_fields = ('sub_discipline', 'work_package_type','project_phase')
    list_filter = ('sub_discipline',)


admin.site.register(Wp_type, Wp_typeModelAdmin)
admin.site.register(Standard_activities, Standard_activitiesModelAdmin)
