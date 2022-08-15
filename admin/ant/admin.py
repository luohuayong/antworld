from django.contrib import admin
from ant.models import Subfamily,Genus,BaseData

# Register your models here.
class SubfamilyAdmin(admin.ModelAdmin):
    pass

class GenusAdmin(admin.ModelAdmin):
    pass

class BaseDataAdmin(admin.ModelAdmin):
    list_display = ('chinese_name','latin_name','other_name')

admin.site.register(Subfamily,SubfamilyAdmin)
admin.site.register(Genus,GenusAdmin)
admin.site.register(BaseData,BaseDataAdmin)