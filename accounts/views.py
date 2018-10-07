from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.forms import RegisterForm, UserLoginForm, UserVerificationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from accounts.serializers import UserSerializer, LoginSerializer
from django.views import generic
from django.urls import reverse_lazy
from accounts.models import User, UserVerify
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
import random
from accounts.permissions import ListAdminOnly, AnonCreateAndUpdateOwnerOnly


class UserLoginView(FormView):
	form_class = UserLoginForm
	template_name = 'login.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		user = authenticate(
			username=request.POST['username'],
			password=request.POST['password']
		)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('welcome'))
			else:
				self.request.session['otp-redirect'] = True
				user_verify_obj = UserVerify.objects.get_or_create(owner=user)[0]
				if user_verify_obj.verify_code is None:
					otp = random.randint(10**6, 10**7 - 1)
					user_verify_obj.verify_code = otp

					# user_verify_obj.send_sms()

					user_verify_obj.save()

				# 	Check the console output for the otp, for now.
				user_verify_obj.print_otp_to_console()
				return HttpResponseRedirect(reverse('accounts:otp_verify', kwargs={'pk': user.mobile}))
		else:
			return HttpResponse('User does not exist')  # TEMP
			# raise forms.ValidationError('Either username or password is incorrect, or user does not exist.')


class OtpVerify(FormView):
	form_class = UserVerificationForm
	template_name = 'validate.html'

	def get(self, request, *args, **kwargs):
		if 'otp-redirect' not in self.request.session:
			return HttpResponse('Not Allowed!')
		else:
			del self.request.session['otp-redirect']
			form = self.form_class(initial=self.initial)
			return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		user = User.objects.all().filter(mobile=kwargs['pk'])[0]
		if user is not None:
			user_verify_obj = UserVerify.objects.get_or_create(owner=user)[0]
			# form = self.form_class(request.POST)
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('welcome'))
			else:
				if request.POST['verify_code'] == user_verify_obj.verify_code:
					user.active = True
					user.save()
					return HttpResponseRedirect(reverse('accounts:login'))
		else:
			return HttpResponse("User does not exist.") 	# TEMP


class SignUp(generic.CreateView):
	form_class = RegisterForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'


@login_required
def profile(request):
	return render(request, 'profile.html', {})


#########################################################################################
# Api Views Below this point.
#########################################################################################
@method_decorator(csrf_exempt, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('mobile')
	serializer_class = UserSerializer
	lookup_field = 'mobile'

	# Custom permissions are used.
	permission_classes = (ListAdminOnly, AnonCreateAndUpdateOwnerOnly)

	# authentication_classes = (BasicAuthentication, SessionAuthentication, TokenAuthentication)
	authentication_classes = (TokenAuthentication, SessionAuthentication, )


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
	def post(self, request):
		serializer = LoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data["user"]
		if user.is_active:
			login(request, user)
			token, created = Token.objects.get_or_create(user=user)
			return Response({"token": token.key}, status=200)
		else:
			msg = "User is not active. Please verify with otp."
			return Response({"error": msg})


@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
	authentication_classes = (TokenAuthentication, )

	def post(self, request):
		logout(request)
		return Response(status=204)


class ValidateView(APIView):

	def post(self, request):
		pass
