# -*- coding: utf-8 -*-

import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# from accounts.views import auth

# Create your tests here.


def login_shortcut(self, username, password):
    return self.client.login(username=username, password=password)


def signup_shortcut(self, username, email, password, password_verify, birthday, home):
    return self.client.post("/accounts/create_account/", {
        'username': username,
        'email': email,
        'password': password,
        'password_verify': password_verify,
        'birthday': birthday,
        'home': home
    })


class AuthenticationTest(TestCase):
    # set up something to tests here, this will be created and destroyed automatically on each time tests is running
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
        self.assertContains(response, "you haven't log in")


    def test_login_with_invalid_credentials(self):
        login_shortcut(self, "admin", "123456")

        response = self.client.get(reverse('accounts:detail'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "you haven't log in")


    def test_login_with_valid_credentials(self):
        login_shortcut(self, "example", "example")

        response = self.client.get(reverse('accounts:detail'))
        self.assertContains(response, "Hi, example")
        self.assertNotContains(response, "you haven't log in")


    def test_logout_from_logged_in(self):
        login_shortcut(self, "example", "example")

        self.client.get(reverse('accounts:logout'))
        response = self.client.get(reverse('accounts:detail'))
        self.assertContains(response, "you haven't log in")
        self.assertNotContains(response, "Hi")


    def test_logout_without_logged_in(self):
        self.client.get(reverse('accounts:logout'))
        response = self.client.get(reverse('accounts:detail'))
        self.assertContains(response, "you haven't log in")
        self.assertNotContains(response, "Hi")


    def test_signup_with_correct_info(self):
        response = signup_shortcut(self, "example_for_signup", "example@example.com", "example", "example",
                                   "1994-08-22", 'Hanoi')
        self.assertContains(response, "registry successfully")
        self.assertNotContains(response, "email address is invalid")


    def test_signup_with_invalid_email(self):
        response = signup_shortcut(self, "example_for_signup", "example1234", "example", "example",
                                   "1994-08-22", 'Hanoi')
        self.assertContains(response, "email address is invalid")
        self.assertNotContains(response, "registry successfully")


    def test_signup_with_already_taken_username(self):
        signup_shortcut(self, "example_for_signup", "example1234@a.com", "example", "example",
                        "1994-08-22", 'Hanoi')
        response = signup_shortcut(self, "example_for_signup", "example1234@a.com", "example", "example",
                                   "1994-08-22", 'Hanoi')
        self.assertContains(response, "username is not available")
        self.assertNotContains(response, "registry successfully")


    def test_signup_with_passwords_not_match(self):
        response = signup_shortcut(self, "example_for_signup", "example1234@a.com", "example123456", "example",
                                   "1994-08-22", 'Hanoi')
        self.assertContains(response, "password not matched")
        self.assertNotContains(response, "registry successfully")

