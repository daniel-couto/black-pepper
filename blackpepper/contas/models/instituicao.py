from django.db import models
from .tipo_institituicao import TipoInstituicao

class Instituicao(models.Model):
    nome = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default=""
    )
    tipo_instituicao = models.ManyToManyField(TipoInstituicao)
    saldo_inicial = models.DecimalField(default=0, decimal_places=2, max_digits=15)

    def __str__(self):
        return self.nome