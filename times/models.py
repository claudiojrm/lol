from django.db import models

class Times(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='times/')
    abreviatura = models.CharField(max_length=5)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']