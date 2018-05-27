from rest_framework import serializers
from parking.models import ParkingLot, ParkingSlot


class ParkingLotSerializer(serializers.ModelSerializer):
	class Meta:
		model = ParkingLot
		fields = ('id', 'longitude', 'latitude', 'location', 'isFull')


class ParkingSlotSerializer(serializers.ModelSerializer):
	class Meta:
		model = ParkingSlot
		fields = ('lot', 'parked_user', 'isOccupied')
