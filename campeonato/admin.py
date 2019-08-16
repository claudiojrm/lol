from django.contrib import admin

# Register your models here.
from django.contrib import admin
from campeonato.models import Campeonato

# Register your models here.
class CampeonatoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Campeonato, CampeonatoAdmin)