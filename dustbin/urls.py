from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url, include
from rest_framework import routers


app_name = 'dustbin'

router = routers.DefaultRouter()
router.register(r'dustbins', views.DustBinViewSet)

urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r"^$", views.DustBinListView.as_view(), name="dustbin_list"),
	url(r"^(?P<pk>\d+)/$", views.DustBinDetailView.as_view(), name="dustbin_detail"),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
