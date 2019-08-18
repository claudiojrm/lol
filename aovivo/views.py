from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework import viewsets, serializers
from aovivo.models import Partida, Lance
from status.models import Status
from times.models import Times
from times.views import TimesSerializer
from campeonato.views import CampeonatoSerializer

def aovivo(request, regiao, campeonato, slug):
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
    partida.status = partida.lances.first().status
    partida.stats = { 
        'blue' : [],
        'red' : [] 
    }

    for lance in partida.lances:
        if ('Encerrado' in lance.status.nome) or ('Pós' in lance.status.nome):
            lance.fim = True

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
        
class PartidaSerializer(serializers.HyperlinkedModelSerializer):
    campeonato = CampeonatoSerializer()
    redside = TimesSerializer()
    blueside = TimesSerializer()

    class Meta:
        model = Partida
        fields = '__all__'
        extra_kwargs = {
            'url': { 
                'lookup_field' : 'slug' 
            }
        }

class PartidaViewSet(viewsets.ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer
    lookup_field = 'slug'