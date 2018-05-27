from django.contrib import admin
from parking.models import ParkingLot, ParkingSlot
# Register your models here.

admin.site.register(ParkingLot)
admin.site.register(ParkingSlot)