from django.db import models
from django.utils.text import slugify

class Regiao(models.Model):
    slug = models.SlugField(unique=True, editable=False)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Regiao, self).save(*args, **kwargs)

    class Meta:
        ordering = ['nome']