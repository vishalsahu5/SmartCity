from django.test import TestCase
from django.urls import reverse, resolve
from mixer.backend.django import mixer
import pytest


class TestUrls(TestCase):
    def test_signup_url(self):
        self.assertIn(resolve('/accounts/signup/').view_name, 'accounts:signup')

    def test_login_url(self):
        self.assertIn(resolve('/accounts/login/').view_name, 'accounts:login')

    def test_logout_url(self):
        self.assertIn(resolve('/accounts/logout/').view_name, 'accounts:logout')

    def test_profile_url(self):
        self.assertIn(resolve('/accounts/profile/').view_name, 'accounts:profile')
