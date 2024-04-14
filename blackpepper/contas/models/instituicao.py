from django.db import models
from _patterns.models import ModelBase

class Instituicao(ModelBase):
    nome = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default=""
    )

    def __str__(self):
        return self.nome