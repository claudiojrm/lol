from rest_framework import viewsets, serializers
from times.models import Times

class TimesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Times
        fields = '__all__'

class TimesViewSet(viewsets.ModelViewSet):
    queryset = Times.objects.all()
    serializer_class = TimesSerializer
