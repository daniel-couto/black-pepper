from django.db import models

class RendaFixaTipo(models.Model):
    nome = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        default="")
    fgc = models.BooleanField(default=True)

    def __str__(self):
        return self.nome