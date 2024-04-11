from django.db import models
from .renda_fixa_tipo import RendaFixaTipo
from contas.models import Instituicao, Conta
from configuracoes.models import Indexadores

class RendaFixa(models.Model):
    nome = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default="")
    renda_fixa_tipo = models.ForeignKey(
        RendaFixaTipo, 
        on_delete=models.RESTRICT)
    rentabilidade_pre = models.DecimalField(
        default=0, 
        decimal_places=2, 
        max_digits=3)
    rentabilidade_pos = models.DecimalField(
        default=0, 
        decimal_places=2, 
        max_digits=3)
    rentabilidade_pos_indexador = models.ForeignKey(
        Indexadores, 
        on_delete=models.RESTRICT)
    emissor = models.ForeignKey(
        Instituicao, 
        on_delete=models.RESTRICT)
    conta = models.ForeignKey(
        Conta, 
        on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome