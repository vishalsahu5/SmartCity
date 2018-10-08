from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from dustbin.serializers import DustbinSerializer
from dustbin.models import Dustbin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from accounts.permissions import ListAdminOnly
from rest_framework.authentication import TokenAuthentication,SessionAuthentication


class DustBinListView(LoginRequiredMixin, ListView):
	"""
	ListView that displays all the dustbins
	"""
	model = Dustbin
	template_name = 'dustbin_list.html'


class DustBinDetailView(LoginRequiredMixin, DetailView):
	"""
	DetailView that displays the information of a specific dustbin
	"""

	model = Dustbin
	context_object_name = 'dustbin'
	template_name = 'dustbin_detail.html'


class DustbinShortestPathView(LoginRequiredMixin, TemplateView):
	"""
	DetailView that displays the shortest path to visist all the dustbins
	"""
	model = Dustbin
	template_name = 'dustbin_path.html'


#########################################################################################
# Api Views Below this point.
#########################################################################################
class DustBinViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows dustbins to be viewed or edited.
	"""
	queryset = Dustbin.objects.all()
	serializer_class = DustbinSerializer
	permission_classes = (ListAdminOnly, )
	authentication_classes = (TokenAuthentication, SessionAuthentication)
