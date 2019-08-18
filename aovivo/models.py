from django.db import models
from django.utils.text import slugify
from campeonato.models import Campeonato
from times.models import Times

class Partida(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    descricao = models.TextField()
    flyer = models.ImageField(upload_to='flyer/')
    patch = models.CharField(max_length=10)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.SET_DEFAULT, default='')
    redside = models.ForeignKey(Times, on_delete=models.CASCADE, related_name='redside')
    blueside = models.ForeignKey(Times, on_delete=models.CASCADE, related_name='blueside')
    kill_redside = models.IntegerField(default=0)
    kill_blueside = models.IntegerField(default=0)
    gold_redside = models.IntegerField(default=0)
    gold_blueside = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

class Lance(models.Model):
    cstatus = ((1, 'Pré jogo'), (2, 'Pick e Bans'), (3, 'Em andamento'), (4, 'Jogo Pausado'), (5, 'Pós Jogo'), (6, 'Encerrado'))
    cstats = (('barao|Barão de Nashor', 'Barão de Nashor'),('dragao-anciao|Dragão ancião', 'Dragão ancião'),('dragao-infernal|Dragão infernal', 'Dragão infernal'),('dragao-montanha|Dragão da montanha', 'Dragão da montanha'),('dragao-oceano|Dragão do oceano', 'Dragão do oceano'),('dragao-vento|Dragão de vento', 'Dragão de vento'))
    cside = (('blue','Blue'), ('red', 'Red'))
    cembed = (('youtube', 'Youtube'), ('twitch', 'Twitch'), ('twitter', 'Twitter'))

    status = models.IntegerField(choices=cstatus, default=1)
    order = models.IntegerField()
    side = models.CharField(max_length=10, choices=cside, blank=True)
    tempo = models.IntegerField(blank=True, default=0)
    titulo = models.CharField(max_length=200, blank=True)
    descricao = models.TextField(blank=True)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    link = models.URLField(blank=True)
    stats = models.CharField(max_length=50, choices=cstats, blank=True)
    embed = models.CharField(max_length=20, choices=cembed, blank=True)
    conteudo_embed = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['order']