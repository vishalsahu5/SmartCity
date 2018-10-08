from django.test import TestCase
from django.urls import reverse, resolve
from mixer.backend.django import mixer
import pytest
from accounts.models import User


class RegisterationTestCase(TestCase):

	def setUp(self):
		self.user = User.objects.create_user(email='abc@gmail.com', mobile='40803403', password='abc_pass')
		self.staffuser = User.objects.create_staffuser(email='xyz@gmail.com', mobile='40889403', password='xyz_pass')

	def test_email_label(self):
		field_label = self.user._meta.get_field('email').verbose_name
		self.assertEquals(field_label, 'email address')

	def test_moblile_label(self):
		testuser = User.objects.get(id=1)
		field_label = testuser._meta.get_field('mobile').verbose_name
		self.assertEquals(field_label, 'mobile number')

	def test_email_max_length(self):
		testuser = User.objects.get(id=1)
		max_length = testuser._meta.get_field('email').max_length
		self.assertEquals(max_length, 255)

	def test_moblile_max_length(self):
		testuser = User.objects.get(id=1)
		max_length = testuser._meta.get_field('mobile').max_length
		self.assertEquals(max_length, 11)
		self.assertTrue(max_length != 34)

	def test_get_full_name(self):
		testuser = User.objects.get(id=1)
		self.assertEquals(testuser.get_full_name(), testuser.email)

	def test_is_user_staff_user(self):
		testuser = User.objects.get(id=1)
		self.assertEquals(testuser.staff, False)

	def test_is_staff_user(self):
		testuser = User.objects.get(id=2)
		self.assertEquals(testuser.staff, True)

	def test_is_active_user(self):
		testuser = User.objects.get(id=1)
		self.assertEquals(testuser.active, False)

	def test_is_active_staff_user(self):
		testuser = User.objects.get(id=2)
		self.assertEquals(testuser.active, True)
