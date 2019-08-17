from django.contrib import admin
from aovivo.models import Partida, Lance
from adminsortable2.admin import SortableInlineAdminMixin

class LanceAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Lance
    extra = 1

class PartidaAdmin(admin.ModelAdmin):
    inlines = (LanceAdmin, )

admin.site.register(Partida, PartidaAdmin)