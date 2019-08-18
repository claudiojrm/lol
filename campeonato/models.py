from django.db import models
from regiao.models import Regiao
from django.utils.text import slugify

class Campeonato(models.Model):
    slug = models.SlugField(editable=False)
    nome = models.CharField(max_length=100)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['nome']