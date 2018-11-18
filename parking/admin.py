from django.contrib import admin
from parking.models import ParkingLot, ParkingSlot, Booking
# Register your models here.

admin.site.register(ParkingLot)
# admin.site.register(ParkingSlot)
admin.site.register(Booking)
