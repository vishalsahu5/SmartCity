from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url, include
from rest_framework import routers


app_name = 'parking'

router = routers.DefaultRouter()
router.register(r'parking_lots', views.ParkingLotViewSet)
router.register(r'parking_slots', views.ParkingSlotViewSet)

urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
