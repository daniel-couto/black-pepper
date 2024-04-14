from django.db import models

# from configuracoes.models import Indexadores
from .instituicao import Instituicao
# from ativos.models import Ativo
from _patterns.models import ModelBase

class Conta(ModelBase):
    instituicao = models.ForeignKey(
        Instituicao, 
        on_delete=models.RESTRICT)
    nome = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default=""
    )
    agencia = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        default=""
    )
    conta = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default=""
    )
    saldo_inicial = models.DecimalField(
        default=0, 
        decimal_places=2,
        max_digits=32)

    def __str__(self):
        return self.nome