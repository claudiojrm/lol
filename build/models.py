from django.db import models

class Build(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField()
    
    class Meta:
        ordering = ['nome']