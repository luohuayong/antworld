from django.contrib import admin
from ant.models import Subfamily,Genus,BaseData,Media

# Register your models here.
class SubfamilyAdmin(admin.ModelAdmin):
    pass

class GenusAdmin(admin.ModelAdmin):
    pass

class MediaAdmin(admin.StackedInline):
    model = Media

class BaseDataAdmin(admin.ModelAdmin):
    list_display = ('chinese_name','latin_name','other_name')
    inlines = [MediaAdmin]



admin.site.register(Subfamily,SubfamilyAdmin)
admin.site.register(Genus,GenusAdmin)
admin.site.register(BaseData,BaseDataAdmin)