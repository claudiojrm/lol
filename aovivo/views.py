from django.shortcuts import render
from aovivo.models import Partida, Lance
from times.models import Times
from django.conf import settings
from django.shortcuts import redirect

def aovivo(request, regiao, campeonato, slug):
    status = ('', 'Pré Jogo', 'Pick e Bans', 'Em andamento', 'Jogo Pausado', 'Fim de Jogo', 'Pós Jogo', 'Encerrado')
    
    try:
        partida = Partida.objects.get(slug=slug, campeonato__slug=campeonato, campeonato__regiao__slug=regiao)
    except Partida.DoesNotExist:
        partida = None

    if not partida:
        return redirect('/')

    partida.lances = Lance.objects.filter(partida=partida.id).reverse()
    
    partida.redside = Times.objects.get(redside=partida.id)
    partida.redside.kill = partida.kill_redside
    partida.redside.gold = partida.gold_redside
    partida.redside.fgold = '{0:,}'.format(partida.gold_redside)
    partida.blueside = Times.objects.get(blueside=partida.id)
    partida.blueside.kill = partida.kill_blueside
    partida.blueside.gold = partida.gold_blueside
    partida.blueside.fgold = '{0:,}'.format(partida.gold_blueside)
    partida.status = status[partida.lances.first().status]
    partida.stats = { 
        'blue' : [],
        'red' : [] 
    }

    for lance in partida.lances:
        lance.fim = True if lance.status > 5 else False
        lance.status = status[lance.status]

        if lance.stats:
            stats = lance.stats.split('|')
            partida.stats[lance.side].append({
                'slug' : stats[0],
                'nome' : stats[1]
            })

    partida.stats['red'].sort(key=lambda x:x['slug'].split('-')[0])
    partida.stats['blue'].sort(key=lambda x:x['slug'].split('-')[0])
    
    return render(request, 'aovivo.html', {
        'MEDIA_URL' : settings.MEDIA_URL,
        'partida' : partida
    })