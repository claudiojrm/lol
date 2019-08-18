from rest_framework import viewsets, serializers
from jogador.models import Jogador

class JogadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'

class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer