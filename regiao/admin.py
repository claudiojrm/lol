from django.contrib import admin
from regiao.models import Regiao

class RegiaoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Regiao, RegiaoAdmin)