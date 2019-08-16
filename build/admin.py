from django.contrib import admin
from build.models import Build
from django.utils.html import format_html
from django.conf import settings

class BuildAdmin(admin.ModelAdmin):
    list_display = ('foto', 'nome')
    search_fields = ('nome',)

    def foto(self, obj):
        return format_html(f'<img src="{settings.MEDIA_URL}{obj.imagem}" width="80">')

admin.site.register(Build, BuildAdmin)