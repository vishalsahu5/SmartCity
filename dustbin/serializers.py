from rest_framework import serializers
from dustbin.models import Dustbin
# class UserSerializer(serializers.HyperlinkedModelSerializer):


class DustbinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dustbin
        fields = ('id', 'longitude', 'latitude', 'location', 'isFull')