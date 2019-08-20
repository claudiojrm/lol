from django.contrib import admin
from aovivo.models import Partida, Lance
from adminsortable2.admin import SortableInlineAdminMixin

class LanceInlineAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Lance
    extra = 1

class LanceAdmin(admin.ModelAdmin):
    list_display = ('partida', 'titulo', 'status', 'order')
    ordering = ('-partida', '-order')
    search_fields = ('partida__titulo',)

class PartidaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slugs')
    autocomplete_fields = ('campeonato',)
    inlines = (LanceInlineAdmin, )
    
    fields = (
        'titulo',
        'descricao',
        'flyer',
        'campeonato',
        ('blueside', 'kill_blueside', 'gold_blueside', 'torre_blueside'),
        ('redside', 'kill_redside', 'gold_redside', 'torre_redside')
    )

    def slugs(self, obj):
        return '/'.join(('', obj.campeonato.regiao.slug,obj.campeonato.slug, obj.slug, ''))

admin.site.register(Partida, PartidaAdmin)
admin.site.register(Lance, LanceAdmin)