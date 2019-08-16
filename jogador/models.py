from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='jogador/')
    choices = (
        ('adc', 'AD Carry'),
        ('jungle', 'Jungle'),
        ('mid', 'Mid Laner'),
        ('suporte', 'Suporte'),
        ('top', 'Top laner'),
    )
    
    nacionalidade = models.CharField(max_length=100, blank=True, default='')
    posicao = models.CharField(max_length=10, choices=choices)

    def __str__(self):
        return self.nome