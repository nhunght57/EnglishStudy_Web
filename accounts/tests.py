import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from accounts.views import auth

# Create your tests here.
class AuthenticationTest(TestCase):
    # def test_login_with_no_credentials(self):
    #     request = self.client.post(reverse('accounts:auth'))
    #     response = auth(request)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertContains(response, "Invalid login")

    def test_login_with_invalid_credentials(self):
        self.client.login(user='admin', password='admin')
        response = self.client.get(reverse('accounts:auth'))
        # response = auth(request)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Welcome admin")