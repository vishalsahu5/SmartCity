from rest_framework import serializers
from accounts.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('mobile', 'email')
