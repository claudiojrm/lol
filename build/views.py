from django.shortcuts import render
from rest_framework import viewsets
from build.serializers import BuildSerializer
from build.models import Build

class BuildViewSet(viewsets.ModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer