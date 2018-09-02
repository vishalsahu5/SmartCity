from django.db import models
from accounts.models import User


class ParkingLot(models.Model):

	moderator = models.OneToOneField(to=User, on_delete=models.DO_NOTHING, null=True, default=None)

	longitude = models.FloatField(null=True)
	latitude = models.FloatField(null=True)
	location = models.CharField(max_length=500, null=True)
	city = models.CharField(max_length=50, null=True)
	state = models.CharField(max_length=50, null=True)
	parked_users = models.PositiveIntegerField(default=0)
	isFull = models.BooleanField(default=False)
	price_per_hour = models.FloatField(default=0)

	def __str__(self):
		return "Parking Lot " + str(self.id)


class ParkingSlot(models.Model):

	lot = models.OneToOneField(on_delete=models.CASCADE, to=ParkingLot)
	parked_user = models.OneToOneField(default=None, to=User, blank=True, null=True, on_delete=models.DO_NOTHING)
	isOccupied = models.BooleanField(default=False)

	def __str__(self):
		return str(self.lot.id) + " SLOT " + str(self.id)