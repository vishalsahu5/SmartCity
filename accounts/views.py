from django.shortcuts import render
from accounts.forms import UserForm, ProfileForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from accounts.serializers import UserSerializer, GroupSerializer, ProfileSerializer
from accounts.models import Profile


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Profile.objects.all().order_by('id')
	serializer_class = ProfileSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


def signup(request):
	if request.method == 'POST':

		user_form = UserForm(data=request.POST)
		profile_form = ProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)

			profile.user = user
			profile.save()

			return HttpResponseRedirect(reverse('accounts:login'))
		else:
			# One of the forms was invalid if this else gets called.
			print(user_form.errors, profile_form.errors)

	else:
		# Was not an HTTP post so we just render the forms as blank.
		user_form = UserForm()
		profile_form = ProfileForm()

	# This is the render and context dictionary to feed
	# back to the signup.html file page.
	context = {'user_form': user_form, 'profile_form': profile_form}
	return render(request, 'signup.html', context)

