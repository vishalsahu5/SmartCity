from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers


app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
	# url(r"login/$", auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r"login/$", views.UserLoginView.as_view(), name='login'),
	url(r"logout/$", auth_views.logout, name="logout"),
	url(r"signup/$", views.SignUp.as_view(), name="signup"),
	url(r"profile/$", views.profile, name="profile"),
	url(r"otp_verify/(?P<pk>\d+)/$", views.OtpVerify.as_view(), name="otp_verify"),
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
