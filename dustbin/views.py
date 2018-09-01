from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from dustbin.serializers import DustbinSerializer
from dustbin.models import Dustbin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView


class DustBinViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows dustbins to be viewed or edited.
	"""
	queryset = Dustbin.objects.all()
	serializer_class = DustbinSerializer


class DustBinListView(LoginRequiredMixin, ListView):
	"""
	Listview that displays all the dustbins
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
