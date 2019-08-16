from django.contrib import admin
from aovivo.models import Partida, Lance

class LanceAdmin(admin.TabularInline):
    model = Lance

class PartidaAdmin(admin.ModelAdmin):
    inlines = (LanceAdmin, )
    exclude = ('lances',)
    pass

admin.site.register(Partida, PartidaAdmin)