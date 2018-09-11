from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)
from sinchsms import SinchSMS


class UserManager(BaseUserManager):
	def create_user(self, email, mobile, password=None):
		"""
		Creates and saves a User with the given email, mobile and password.
		"""
		if not mobile:
			raise ValueError('Users must have a mobile number')

		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.mobile = mobile
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, mobile, password):
		"""
		Creates and saves a staff user with the given email and password.
		"""
		user = self.create_user(
			email,
			mobile=mobile,
			password=password
		)
		user.active = True
		user.staff = True
		user.save(using=self._db)
		return user

	def create_superuser(self, email, mobile, password):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(
			email,
			mobile=mobile,
			password=password
		)
		user.active = True
		user.staff = True
		user.admin = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	mobile = models.CharField(
		verbose_name='mobile number',
		unique=True,
		max_length=11,
		default=None,
	)
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)

	active = models.BooleanField(default=False)
	staff = models.BooleanField(default=False)  # a admin user; non super-user
	admin = models.BooleanField(default=False)  # a superuser
	# notice the absence of a "Password field", that's built in.
	objects = UserManager()

	USERNAME_FIELD = 'mobile'
	REQUIRED_FIELDS = ['email']  # Mobile & Password are required by default.

	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __str__(self):  # __unicode__ on Python 2
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.staff

	@property
	def is_admin(self):
		"Is the user a admin member?"
		return self.admin

	@property
	def is_active(self):
		"Is the user active?"
		return self.active


class UserVerify(models.Model):
	"""
	Model used for verifying users via otp
	"""
	owner = models.ForeignKey(to=User)
	verify_code = models.CharField(
		max_length=254,
		null=True,
		default=None,
		verbose_name='OTP'
	)

	def send_sms(self):
		"""
		TODO : Use twilio/sinch API to actually send sms to mobile phone
		:return:
		"""
		number = '+91' + self.owner.mobile
		message = self.verify_code
		client = SinchSMS('d9abf26d-0ec2-49f3-af2c-17cda14911a4', 'C1sG5vRbskaqWB37kUKMPg==')

		print("Sending '%s' to %s" % (message, number))
		response = client.send_message(number, message)
		message_id = response['messageId']
		response = client.check_status(message_id)

		while response['status'] != 'Successful':
			print(response['status'])
			time.sleep(1)
			response = client.check_status(message_id)

		print(response['status'])

	# print("OTP -----> " + str(self.verify_code))

	def print_otp_to_console(self):
		"""
		A useless function to print otp to console to authenticate users while the sms
		feature is not ready.
		:return:
		"""
		print("OTP -----> " + str(self.verify_code))
