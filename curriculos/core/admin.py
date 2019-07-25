from django.contrib import admin
from core.models import Curriculo
from django.utils.safestring import mark_safe

class CurriculoAdmin(admin.ModelAdmin):

    list_display = ('name','description','image','start_date','create_at')
    search_fields = ['name']


admin.site.register(Curriculo,CurriculoAdmin)
