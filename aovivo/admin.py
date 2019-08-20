from django.contrib import admin
from aovivo.models import Partida, Lance
from adminsortable2.admin import SortableInlineAdminMixin

class LanceAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Lance
    extra = 1

class PartidaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slugs')
    inlines = (LanceAdmin, )
    autocomplete_fields = ('campeonato', 'blueside', 'redside')
    
    fields = (
        'titulo',
        'descricao',
        'flyer',
        'campeonato',
        ('blueside', 'kill_blueside', 'gold_blueside'),
        ('redside', 'kill_redside', 'gold_redside')
    )

    def slugs(self, obj):
        return '/'.join(('', obj.campeonato.regiao.slug,obj.campeonato.slug, obj.slug, ''))

admin.site.register(Partida, PartidaAdmin)