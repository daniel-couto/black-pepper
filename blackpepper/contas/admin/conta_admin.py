from django.contrib import admin
from contas.models.conta import Conta
from admin_totals.admin import ModelAdminTotals
from django.db.models import Sum
from django.db.models.functions import Coalesce
from _patterns.admin import ModelAdminBase

@admin.register(Conta)
class ContaAdmin(ModelAdminBase, ModelAdminTotals):
    model = Conta
    list_display = ['nome', 'saldo_inicial']
    list_totals = [('saldo_inicial', lambda field: Sum(field))]
