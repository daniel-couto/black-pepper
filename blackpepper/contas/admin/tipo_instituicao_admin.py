from django.contrib import admin
from contas.models.tipo_institituicao import TipoInstituicao

class TipoInstituicaoAdmin(admin.AdminSite):
    display_list = ("nome")

admin.site.register(TipoInstituicao)