from django.contrib import admin
from jogador.models import Jogador
from django.utils.html import format_html
from django.conf import settings

class JogadorAdmin(admin.ModelAdmin):
    list_display = ('foto', 'nome', 'posicao')
    search_fields = ('nome',)

    def foto(self, obj):
        return format_html(f'<img src="{settings.MEDIA_URL}{obj.imagem}" width="80">')

admin.site.register(Jogador, JogadorAdmin)