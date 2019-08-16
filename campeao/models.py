from django.db import models

class Campeao(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='campeao/')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']