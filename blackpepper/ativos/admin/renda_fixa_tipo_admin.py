from django.contrib import admin
from ativos.models.renda_fixa import RendaFixaTipo

@admin.register(RendaFixaTipo)
class RendaFixaTipoAdmin(admin.ModelAdmin):
    display_list = ("nome")