from django.contrib import admin
from ativos.models.renda_fixa import RendaFixa

@admin.register(RendaFixa)
class RendaFixaAdmin(admin.ModelAdmin):
    display_list = ("nome")