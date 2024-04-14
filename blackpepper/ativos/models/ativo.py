from django.db import models
from contas.models import Instituicao, Conta
from configuracoes.models import Indexadores
from _patterns.models import ModelBase

class Ativo(ModelBase):
    conta_id = models.ForeignKey(
        Conta, 
        on_delete=models.RESTRICT)
    conta_primaria = models.BooleanField("Conta primária", blank=True, null=False, default=False)
    nome = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default="")
    saldo_inicial = models.DecimalField(
        default=0, 
        decimal_places=2, 
        max_digits=16)
    rentabilidade_pos_indexador = models.ForeignKey(
        Indexadores,
        on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome