from django.contrib import admin
from aovivo.models import Partida, Lance

class LanceAdmin(admin.StackedInline):
    model = Lance

class PartidaAdmin(admin.ModelAdmin):
    inlines = (LanceAdmin, )

admin.site.register(Partida, PartidaAdmin)