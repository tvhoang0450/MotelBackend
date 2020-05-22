from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import PhongTroListCreateAPIView

app_name = 'PhongTro'

router = routers.DefaultRouter()
router.register(r'posts', views.PhongTroListCreateAPIView, basename="Posts")
router.register(r'posts', views.PhongTroUpdateDeleteAPIView, basename="Posts")
urlpatterns = [
    url('^api/', include(router.urls)),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]