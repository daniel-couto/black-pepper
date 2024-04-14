from django.contrib import admin
from contas.models.instituicao import Instituicao
from _patterns.admin import ModelAdminBase

@admin.register(Instituicao)
class InstituicaoAdmin(ModelAdminBase):
    model = Instituicao
    list_display = ['nome']
        