from rest_framework import serializers
from build.models import Build

class BuildSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Build
        fields = ['nome', 'imagem']