from django.contrib.auth.models import User, Group
from rest_framework import serializers
from accounts.models import Profile
# class UserSerializer(serializers.HyperlinkedModelSerializer):


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'mobile')