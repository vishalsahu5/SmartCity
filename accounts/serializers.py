from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.models import User, UserVerify
from rest_framework import exceptions
import random


class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	active = serializers.BooleanField(read_only=True)
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = User
		fields = ('mobile', 'email', 'password', 'active', 'id')

	def create(self, validated_data):
		user = super(UserSerializer, self).create(validated_data)
		user.set_password(validated_data['password'])

		# For now, the user is active. In future, user will not be active by default.
		user.active = True

		user.save()
		return user


class LoginSerializer(serializers.Serializer):
	def create(self, validated_data):
		pass

	def update(self, instance, validated_data):
		pass

	username = serializers.CharField()
	password = serializers.CharField()

	def validate(self, data):
		username = data.get("username", "")
		password = data.get("password", "")

		if username and password:
			user = authenticate(username=username, password=password)
			if user:

				if not user.is_active:
					user_verify_obj = UserVerify.objects.get_or_create(owner=user)[0]
					if user_verify_obj.verify_code is None:
						otp = random.randint(10 ** 6, 10 ** 7 - 1)
						user_verify_obj.verify_code = otp

						# user_verify_obj.send_sms()

						user_verify_obj.save()

					# 	Check the console output for the otp, for now.
					user_verify_obj.print_otp_to_console()

				data["user"] = user

			else:
				msg = "Unable to login with given credentials."
				raise exceptions.ValidationError(msg)
		else:
			msg = "Must provide both username and password."
			raise exceptions.ValidationError(msg)
		return data


class UserVerifySerializer(serializers.Serializer):
	def create(self, validated_data):
		pass

	def update(self, instance, validated_data):
		pass
