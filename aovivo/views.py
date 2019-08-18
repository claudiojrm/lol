from django.shortcuts import render
from aovivo.models import Partida, Lance
from times.models import Times
from django.conf import settings
from django.shortcuts import redirect

def aovivo(request, regiao, campeonato, slug):
    status = ('', 'Pré Jogo', 'Pick e Bans', 'Em andamento', 'Jogo Pausado', 'Pós Jogo', 'Encerrado')
    
    try:
        partida = Partida.objects.get(slug=slug, campeonato__slug=campeonato, campeonato__regiao__slug=regiao)
    except Partida.DoesNotExist:
        partida = None

    if not partida:
        return redirect('/')

    partida.lances = Lance.objects.filter(partida=partida.id).reverse()
    
    partida.redside = Times.objects.get(redside=partida.id)
    partida.redside.kill = partida.kill_redside
    partida.blueside = Times.objects.get(blueside=partida.id)
    partida.blueside.kill = partida.kill_blueside
    partida.status = status[partida.lances.first().status]

    for lance in partida.lances:
        if lance.status > 4:
            lance.fim = True

        lance.status = status[lance.status]
    

    return render(request, 'aovivo.html', {
        'MEDIA_URL' : settings.MEDIA_URL,
        'partida' : partida
    })