from django.contrib import admin
from .models import Disease, Record, Symptom, Relation
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export.fields import Field

admin.site.register(Record)
admin.site.register(Relation)

class DiseaseResource(resources.ModelResource):

    class Meta:
        model = Disease



class DiseaseAdmin(ImportExportActionModelAdmin):
    resource_class = DiseaseResource


admin.site.register(Disease, DiseaseAdmin)

class SympResource(resources.ModelResource):

    class Meta:
        model = Symptom


class SympAdmin(ImportExportActionModelAdmin):
    resource_class = SympResource


admin.site.register(Symptom, SympAdmin)

