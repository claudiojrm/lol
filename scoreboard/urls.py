"""scoreboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from build.views import BuildViewSet
from campeao.views import CampeaoViewSet
from campeonato.views import CampeonatoViewSet
from jogador.views import JogadorViewSet
from regiao.views import RegiaoViewSet
from times.views import TimesViewSet
from aovivo.views import PartidaViewSet

router = routers.DefaultRouter()
router.register(r'build', BuildViewSet)
router.register(r'campeao', CampeaoViewSet)
router.register(r'campeonato', CampeonatoViewSet)
router.register(r'jogador', JogadorViewSet)
router.register(r'regiao', RegiaoViewSet)
router.register(r'times', TimesViewSet)
router.register(r'partida', PartidaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aovivo.urls')),
    path('ao-vivo/', include('aovivo.urls')),
    path('api/', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)