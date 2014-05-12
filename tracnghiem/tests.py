# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse

from tracnghiem.models import Question

# Create your tests here.

def create_questions(question_text):
    return Question.objects.create(question_text = question_text)


class TracnghiemMethodsTest(TestCase):
    # Set up an account to simulate that user is logged in
    def setUp(self):
        username = "example"
        password = "example"
        user = User.objects.create_user(username=username, password=password)
        user.save()
        self.client.login(username=username, password=password)


    # While logged in, but there are no questions in database, an appropriate message should be displayed
    # instead of a blank page
    def test_view_with_no_questions_logged_in(self):

        response = self.client.get(reverse('tracnghiem:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Không có gì")
        self.assertQuerysetEqual(response.context['list_of_questions'], [])

    # While logged in and there is one question in database, it should be displayed
    def test_view_with_one_question_logged_in(self):
        create_questions("Somewhat")
        response = self.client.get(reverse('tracnghiem:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Somewhat")
        self.assertNotContains(response, "Không có gì thú vị ở đây cả")
        self.assertQuerysetEqual(response.context['list_of_questions'], ['<Question: Somewhat>'])

    # While logged out, an appropriate message should be displayed instead of content
    def test_view_logged_out(self):
        create_questions("Somewhat")
        self.client.logout()
        response = self.client.get(reverse('tracnghiem:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bạn chưa đăng nhập")
        self.assertNotContains(response, "Somewhat")