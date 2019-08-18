from rest_framework import viewsets, serializers
from regiao.models import Regiao

class RegiaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regiao
        fields = '__all__'
        extra_kwargs = {
            'url': { 
                'lookup_field' : 'slug' 
            }
        }

class RegiaoViewSet(viewsets.ModelViewSet):
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer
    lookup_field = 'slug'