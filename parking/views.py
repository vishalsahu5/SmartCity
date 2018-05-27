from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from parking.serializers import ParkingLotSerializer, ParkingSlotSerializer
from parking.models import ParkingSlot, ParkingLot


class ParkingSlotViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows parking slots to be viewed or edited.
	"""
	queryset = ParkingSlot.objects.all()
	serializer_class = ParkingSlotSerializer


class ParkingLotViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows parking lots to be viewed or edited.
	"""
	queryset = ParkingLot.objects.all()
	serializer_class = ParkingLotSerializer
