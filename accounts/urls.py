from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers


app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
	url(r"login/$", auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r"logout/$", auth_views.logout, name="logout"),
	url(r"signup/$", views.signup, name="signup"),
	url(r"profile/$", views.profile, name="profile"),
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
