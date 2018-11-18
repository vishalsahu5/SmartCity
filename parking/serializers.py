from rest_framework import serializers
from parking.models import ParkingLot, ParkingSlot, OnStreetParkingSlot, Booking
from accounts.models import User


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


class BookingSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	user = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, queryset=User.objects.all())

	class Meta:
		model = Booking
		fields = '__all__'
