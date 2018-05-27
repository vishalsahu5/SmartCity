from django.db import models
from django.contrib.auth.models import User


class ParkingLot(models.Model):
	longitude = models.FloatField()
	latitude = models.FloatField()
	location = models.CharField(max_length=500)
	isFull = models.BooleanField()

	def __str__(self):
		return "Dustbin " + str(self.id)


class ParkingSlot(models.Model):
	lot = models.OneToOneField(on_delete=models.CASCADE, to=ParkingLot)
	parked_user = models.ForeignKey(default=None, to=User)
	isOccupied = models.BooleanField(default=False)

	def __str__(self):
		return str(self.lot.id) + "SLOT" + str(self.id)