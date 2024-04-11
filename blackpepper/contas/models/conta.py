from django.db import models
from .instituicao import Instituicao

class Conta(models.Model):
    nome = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default=""
    )
    instituicao = models.ForeignKey(
        Instituicao, 
        on_delete=models.RESTRICT)
    saldo_inicial = models.DecimalField(
        default=0, 
        decimal_places=2,
        max_digits=15)

    def __str__(self):
        return self.nome