from django.db import models
from regiao.models import Regiao

class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    regiao = models.ForeignKey(Regiao, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome