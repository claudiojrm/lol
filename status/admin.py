from django.contrib import admin
from status.models import Status

class StatusAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Status, StatusAdmin) 