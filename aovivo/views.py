from django.shortcuts import render
from aovivo.models import Partida, Lance
from times.models import Times
from django.conf import settings

def aovivo(request):
    status = ('Pré Jogo', 'Pick e Bans', 'Em andamento', 'Jogo Pausado', 'Pós Jogo', 'Encerrado')
    partida = Partida.objects.all()[0]
    partida.lances = Lance.objects.filter(partida=partida.id)
    
    partida.redside = Times.objects.get(redside=partida.id)
    partida.redside.kill = partida.kill_redside
    partida.blueside = Times.objects.get(blueside=partida.id)
    partida.blueside.kill = partida.kill_blueside
    partida.status = 1

    for lance in partida.lances:
        if partida.status < lance.status:
            partida.status = lance.status

        lance.status = status[lance.status - 1]

    
    partida.status = status[partida.status - 1]

    return render(request, 'aovivo.html', {
        'MEDIA_URL' : settings.MEDIA_URL,
        'partida' : partida
    })