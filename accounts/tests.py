import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# from accounts.views import auth

# Create your tests here.
class AuthenticationTest(TestCase):
    # set up something to test here, this will be created and destroyed automatically on each time test is running
    def setUp(self):
        user = User.objects.create_user(username='example', password='example')
        user.save()

    '''
        Usage:
        def a_test(self):
            username = "your_username"
            password = "your_password"
            self.client.login(username=username, password = password)

            # NOTICE: this way doesn't work
            # self.client.post("login_url", {'username': username, 'password': password}) #NOT WORKING

            response = self.client.get("your_url")
            # and now assert something with 'response'
    '''

    def test_login_with_no_credentials(self):
        self.client.login(username='', password='')

        response = self.client.get(reverse('accounts:detail'))
        self.assertContains(response, "You're not logged in")


    def test_login_with_invalid_credentials(self):
        username = "example"
        password = "123456"
        self.client.login(username=username, password=password)

        response = self.client.get(reverse('accounts:detail'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "You're not logged in")


    def test_login_with_valid_credentials(self):
        username = "example"
        password = "example"
        self.client.login(username=username, password=password)

        response = self.client.get(reverse('accounts:detail'))
        self.assertContains(response, "You're logged in as " + username)