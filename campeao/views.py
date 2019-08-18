from rest_framework import viewsets, serializers
from campeao.models import Campeao

class CampeaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campeao
        fields = '__all__'

class CampeaoViewSet(viewsets.ModelViewSet):
    queryset = Campeao.objects.all()
    serializer_class = CampeaoSerializer
