from django.db import models

class TipoInstituicao(models.Model):
    nome = models.CharField(
        max_length=128,
        blank=False,
        null=True
    )
    
    def __str__(self):
        return self.nome