from django.db import models
from accounts.models import User


class ParkingLot(models.Model):

	# In the current iteration, moderator is not included. Only admins will be handle it.
	# moderator = models.OneToOneField(to=User, on_delete=models.DO_NOTHING, null=True, default=None)

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

	# The parked user is not active currently.
	# We are not tracking the parked user because it is too expensive to track which user has
	# parked in a slot.

	# parked_user = models.OneToOneField(default=None, to=User, blank=True, null=True, on_delete=models.DO_NOTHING)
	lot = models.OneToOneField(on_delete=models.CASCADE, to=ParkingLot)
	isOccupied = models.BooleanField(default=False)

	def __str__(self):
		return str(self.lot.id) + " SLOT " + str(self.id)


class OnStreetParkingSlot(models.Model):
	longitude = models.FloatField(null=True)
	latitude = models.FloatField(null=True)
	location = models.CharField(max_length=500, null=True)
	city = models.CharField(max_length=50, null=True)
	state = models.CharField(max_length=50, null=True)
	isOccupied = models.BooleanField(default=False)

	# According to our current iteration, we are not charging for the on street parking.
	# Making charging mechanism for on street parking is expensive task for now and requires
	# more infrastructure.

	# price_per_hour = models.FloatField(default=0)
