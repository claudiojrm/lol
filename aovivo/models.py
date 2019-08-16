from django.db import models

class Partida(models.Model):
    titulo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.titulo

class Lance(models.Model):
    titulo = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
