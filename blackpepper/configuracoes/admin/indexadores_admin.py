from django.contrib import admin
from configuracoes.models.indexadores import Indexadores

@admin.register(Indexadores)
class IndexadoresAdmin(admin.ModelAdmin):
    display_list = ("nome")