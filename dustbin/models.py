from django.db import models


# Create your models here.


class Dustbin(models.Model):
	longitude = models.TextField()
	latitude = models.TextField()
	location = models.TextField()
	isFull = models.BooleanField()

	def __str__(self):
		return "Dustbin " + str(self.id)