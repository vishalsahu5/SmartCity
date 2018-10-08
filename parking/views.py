from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from parking.serializers import ParkingLotSerializer, ParkingSlotSerializer, OnStreetParkingSlotSerializer
from parking.models import ParkingSlot, ParkingLot, OnStreetParkingSlot
from accounts.permissions import AnonReadCreateAndUpdateAdminOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


#########################################################################################
# Api Views Below this point.
#########################################################################################
class ParkingSlotViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows parking slots to be viewed or edited.
	"""
	queryset = ParkingSlot.objects.all()
	serializer_class = ParkingSlotSerializer
	permission_classes = (AnonReadCreateAndUpdateAdminOnly,)
	authentication_classes = (TokenAuthentication, SessionAuthentication)


class ParkingLotViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows parking lots to be viewed or edited.
	"""
	queryset = ParkingLot.objects.all()
	serializer_class = ParkingLotSerializer
	permission_classes = (AnonReadCreateAndUpdateAdminOnly,)
	authentication_classes = (TokenAuthentication, SessionAuthentication)


class OnStreetParkingSlotViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows on street parking slots to be viewed or edited.
	"""
	queryset = OnStreetParkingSlot.objects.all()
	serializer_class = OnStreetParkingSlotSerializer
	permission_classes = (AnonReadCreateAndUpdateAdminOnly,)
	authentication_classes = (TokenAuthentication, SessionAuthentication)

