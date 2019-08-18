from rest_framework import viewsets, serializers
from campeonato.models import Campeonato
from regiao.views import RegiaoSerializer

class CampeonatoSerializer(serializers.HyperlinkedModelSerializer):
    regiao = RegiaoSerializer()

    class Meta:
        model = Campeonato
        fields = '__all__'
        extra_kwargs = {
            'url': { 
                'lookup_field' : 'slug' 
            }
        }

class CampeonatoViewSet(viewsets.ModelViewSet):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer
    lookup_field = 'slug'