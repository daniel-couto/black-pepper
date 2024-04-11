from django.contrib import admin
from contas.models.conta import Conta
from admin_totals.admin import ModelAdminTotals
from django.db.models import Sum, Avg
from django.db.models.functions import Coalesce

@admin.register(Conta)
class ContaAdmin(ModelAdminTotals):
    model = Conta
    list_display = ['nome', 'saldo_inicial']
    list_totals = [('saldo_inicial', lambda field: Sum(field))]
