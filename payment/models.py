from django.db import models
from parking.models import ParkingSlot
from django.contrib.auth.models import User
from datetime import datetime


class ParkingPayment(models.Model):
	slot = models.OneToOneField(on_delete=models.DO_NOTHING, to=ParkingSlot)
	parked_user = models.OneToOneField(on_delete=models.DO_NOTHING, to=User)
	arrival = models.DateTimeField(default=datetime.now())
	departure = models.DateTimeField(default=None)

	def __str__(self):
		return str(self.slot) + " -- " + str(self.parked_user)