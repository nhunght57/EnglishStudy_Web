from django.test import TestCase
from django.core.urlresolvers import reverse

from tracnghiem.models import Question

# Create your tests here.

def create_questions(question_text):
    return Question.objects.create(question_text = question_text)


class TracnghiemMethodsTest(TestCase):
    def test_view_with_no_questions(self):
        response = self.client.get(reverse('tracnghiem:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Không có gì")
        self.assertQuerysetEqual(response.context['list_of_questions'], [])

    def test_view_with_one_question(self):
        create_questions("Somewhat")
        response = self.client.get(reverse('tracnghiem:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Somewhat")
        self.assertNotContains(response, "Không có gì thú vị ở đây cả")
        self.assertQuerysetEqual(response.context['list_of_questions'], ['<Question: Somewhat>'])