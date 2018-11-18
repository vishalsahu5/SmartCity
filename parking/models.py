from django.db import models
from accounts.models import User
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from rest_framework import exceptions


class ParkingLot(models.Model):

	# In the current iteration, moderator is not included. Only admins will handle it.
	# moderator = models.OneToOneField(to=User, on_delete=models.DO_NOTHING, null=True, default=None)

	longitude = models.FloatField(null=True)
	latitude = models.FloatField(null=True)
	location = models.CharField(max_length=500, null=True)
	city = models.CharField(max_length=50, null=True)
	state = models.CharField(max_length=50, null=True)
	capacity = models.PositiveIntegerField(default=2)
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
	lot = models.ForeignKey(on_delete=models.CASCADE, to=ParkingLot)
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


class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	parking_lot = models.ForeignKey(ParkingLot, on_delete=models.DO_NOTHING)
	start_time = models.DateTimeField(auto_now_add=True)
	end_time = models.DateTimeField(blank=True, null=True)
	paid = models.BooleanField(default=False)


@receiver(post_save, sender=Booking)
def add_parked_user(sender, **kwargs):
	parking_lot = kwargs['instance'].parking_lot
	if kwargs.get('created', False):
		if not parking_lot.isFull:
			parking_lot.parked_users += 1

			if parking_lot.parked_users == parking_lot.capacity:
				parking_lot.isFull = True
			parking_lot.save()
		else:
			msg = "Parking Lot is Full."
			raise exceptions.ValidationError(msg)
	else:
		parking_lot.parked_users -= 1
		if parking_lot.parked_users < parking_lot.capacity:
			parking_lot.isFull = False
		parking_lot.save()