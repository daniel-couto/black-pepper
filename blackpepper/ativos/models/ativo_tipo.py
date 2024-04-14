from django.db import models
from _patterns.models import ModelBase

class AtivoTipo(ModelBase):
    nome = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default="")
    fgc = models.BooleanField(default=True)

    def __str__(self):
        return self.nome