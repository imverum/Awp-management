from django.db import models

class Wp_type(models.Model):
    sub_discipline = models.CharField('sub_discipline',max_length=200)
    discipline = models.CharField('discipline',max_length=200)
    sub_discipline_id = models.CharField('sub_discipline_id',max_length=200)

    class Meta:
        db_table = 'db_wp_type'
        verbose_name_plural = 'BD Wp Types'
        verbose_name = 'BD Wp Types'

    def __str__(self):
        return self.sub_discipline

class Standard_activities(models.Model):
    sub_discipline = models.CharField('sub_discipline',max_length=200, null = True)
    work_package_type = models.CharField('work_package_type',max_length=200, null = True)
    project_phase = models.CharField('project_phase', max_length=200, null = True)
    discipline = models.CharField('discipline', max_length=200, null = True)
    activity_name = models.CharField('activity_name', max_length=200, null = True)
    standard_activities_id = models.CharField('standard_activities_id',max_length=200)
    predecessor = models.CharField('predecessor',max_length=200, blank=True)
    relation = models.CharField('relation',max_length=200, blank=True)
    lag = models.CharField('lag', max_length=200, blank=True)
    duration = models.CharField('duration', max_length=200, blank=True)
    physical_progress = models.CharField('physical_progress', max_length=200, blank=True)
    financial_progress = models.CharField('financial_progress', max_length=200, blank=True)
    responsible = models.CharField('responsible', max_length=200, blank=True)

    class Meta:
        db_table = 'db_standard_activities'
        verbose_name_plural = 'BD Standard Activities'
        verbose_name = 'BD Standard Activities'

    def __str__(self):
        return self.sub_discipline

