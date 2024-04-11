from django.db import models

class Indexadores(models.Model):
    nome = models.CharField(
        max_length=32,
        blank=False,
        null=False,
        default="")
    valor = models.DecimalField(
        default=0, 
        decimal_places=2, 
        max_digits=3)