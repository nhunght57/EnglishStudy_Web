from django.test import TestCase
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest

# Create your tests here.
from homepage.views import auth


class loginTest(TestCase):
    def test_authentication_with_correct_login(self):
        user = User.objects.create_user('user1', 'Password123')
        user.save()
        request = "POST /accounts/auth/ HTTP/1.1\n\nusername=user1&password=Password123"
        self.assertContains(auth(request), "logged in")