from django.shortcuts import render
from accounts.forms import RegisterForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from accounts.serializers import CustomUserSerializer
from django.views import generic
from django.urls import reverse_lazy
from accounts.models import User


class CustomUserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = CustomUserSerializer


class SignUp(generic.CreateView):
	form_class = RegisterForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'


@login_required
def profile(request):
	return render(request, 'profile.html', {})