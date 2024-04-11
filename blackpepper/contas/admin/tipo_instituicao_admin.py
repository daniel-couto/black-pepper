from django.contrib import admin
from contas.models.tipo_institituicao import TipoInstituicao

@admin.register(TipoInstituicao)
class TipoInstituicaoAdmin(admin.ModelAdmin):
    display_list = ("nome")
