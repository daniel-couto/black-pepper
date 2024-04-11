from django.contrib import admin
from contas.models.instituicao import Instituicao

@admin.register(Instituicao)
class instituicaoAdmin(admin.ModelAdmin):
    model = Instituicao
    list_display = ['nome']
