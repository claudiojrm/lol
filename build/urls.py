from django.urls import include, path
from rest_framework import routers
from build.views import BuildViewSet

router = routers.DefaultRouter()
router.register(r'build', BuildViewSet)

urlpatterns = [
    path('', include(router.urls))
]