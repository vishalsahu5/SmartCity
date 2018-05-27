from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url, include
from rest_framework import routers


app_name = 'dustbin'

router = routers.DefaultRouter()
router.register(r'dustbins', views.DustBinViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
