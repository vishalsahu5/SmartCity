from django.db import models
from django.contrib.auth.models import User


class ParkingLot(models.Model):
	longitude = models.FloatField()
	latitude = models.FloatField()
	location = models.CharField(max_length=500)
	isFull = models.BooleanField()

	def __str__(self):
		return "Parking Lot " + str(self.id)


class ParkingSlot(models.Model):
	lot = models.OneToOneField(on_delete=models.CASCADE, to=ParkingLot)
	parked_user = models.OneToOneField(default=None, to=User, blank=True, null=True, on_delete=models.DO_NOTHING)
	isOccupied = models.BooleanField(default=False)

	def __str__(self):
		return str(self.lot.id) + " SLOT " + str(self.id)