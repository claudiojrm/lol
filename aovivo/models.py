from django.db import models
from campeonato.models import Campeonato
from times.models import Times

class Partida(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    flyer = models.ImageField(upload_to='flyer/')
    patch = models.CharField(max_length=10)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.SET_DEFAULT, default='')
    redside = models.ForeignKey(Times, on_delete=models.CASCADE, related_name='redside')
    blueside = models.ForeignKey(Times, on_delete=models.CASCADE, related_name='blueside')
    kill_redside = models.IntegerField()
    kill_blueside = models.IntegerField()

    def __str__(self):
        return self.titulo

class Lance(models.Model):
    status = models.IntegerField(choices=((1, 'Pré jogo'), (2, 'Pick e Bans'), (3, 'Em andamento'), (4, 'Jogo Pausado'), (5, 'Pós Jogo'), (6, 'Encerrado')), default=1)
    side = models.CharField(max_length=10, choices=(('blue','Blue'), ('red', 'Red')), blank=True)
    tempo = models.IntegerField(blank=True, default=0)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
