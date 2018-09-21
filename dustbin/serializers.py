from rest_framework import serializers
from dustbin.models import Dustbin


class DustbinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dustbin
        fields = ('id', 'longitude', 'latitude', 'location', 'isFull')