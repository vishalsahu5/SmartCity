from rest_framework import serializers
from parking.models import ParkingLot, ParkingSlot, OnStreetParkingSlot


class ParkingLotSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = ParkingLot
		# fields = ('id', 'longitude', 'latitude', 'location', 'isFull')
		fields = '__all__'


class ParkingSlotSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = ParkingSlot
		# fields = ('id', 'lot', 'isOccupied')
		fields = '__all__'


class OnStreetParkingSlotSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = OnStreetParkingSlot
		fields = '__all__'
