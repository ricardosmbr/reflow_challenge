from django.contrib import admin
from core.models import Curriculo
from django.utils.safestring import mark_safe

class CurriculoAdmin(admin.ModelAdmin):

    list_display = ('name','description','image','create_at','update_at')
    search_fields = ['name']


admin.site.register(Curriculo,CurriculoAdmin)
