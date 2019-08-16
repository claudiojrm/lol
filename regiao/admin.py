from django.contrib import admin
from regiao.models import Regiao

# Register your models here.
class RegiaoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Regiao, RegiaoAdmin)