from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from dustbin.serializers import DustbinSerializer
from dustbin.models import Dustbin


class DustBinViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows dustbins to be viewed or edited.
	"""
	queryset = Dustbin.objects.all()
	serializer_class = DustbinSerializer
