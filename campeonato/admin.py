from django.contrib import admin
from campeonato.models import Campeonato

# Register your models here.
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'regiao')
    search_fields = ('nome', 'regiao__nome')

admin.site.register(Campeonato, CampeonatoAdmin)