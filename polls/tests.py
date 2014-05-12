import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from polls.models import Question

# Create your tests here.

# Create a question with the time is now incremented by delta_days, delta_hours
def create_question(question_text, delta_days, delta_hours = 0):
    time = timezone.now() + datetime.timedelta(days = delta_days, hours = delta_hours)
    return Question.objects.create(question_text = question_text, pub_date = time)

class QuestionMethodTest(TestCase):
    # was_published_recently() should return False for questions whose
    # the pub_date is in the future
    def test_was_published_recently_with_future_question(self):
        future_question_example = create_question('', +5)
        self.assertEqual(future_question_example.was_published_recently(), False)


    # was_published_recently() should return False for questions whose
    # the pub_date is older than 1 day
    def test_was_published_recently_with_past_question(self):
        past_question_example = create_question('', -2)
        self.assertEqual(past_question_example.was_published_recently(), False)

    
    # was_published_recently() should return True for questions whose
    # the pub_date is in the recent day
    def test_was_published_recently_with_recent_question(self):
        past_question_example = create_question('', 0, -12)
        self.assertEqual(past_question_example.was_published_recently(), True)
    

    # if no questions exist, an appropriate message should be displayed
    def test_index_view_with_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['all_question_list'], [])


    # question with a pub_date in the past should be displayed on the index page
    def test_index_view_with_a_past_question(self):
        create_question("past question?", -10)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['all_question_list'], ['<Question: past question?>'])


    # question with a pub_date in the future should not be displayed on the index page
    def test_index_view_with_a_future_question(self):
        create_question("future question?", 0, 12)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['all_question_list'], [])


    # if both past and future questions exists, only past questions should be displayed
    def test_index_view_with_both_future_and_past_questions(self):
        create_question("past question?", 0, -19)
        create_question("future question?", 0, 23)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['all_question_list'], ['<Question: past question?>'])


    # with 3 questions, tests the order of them
    def test_index_view_with_some_past_questions(self):
        create_question("tests past question 1?", -1, -7)
        create_question("tests past question 2?", 0, -15)
        create_question("tests past question 3?", 0, -23)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['all_question_list'],
                                 ['<Question: tests past question 2?>',
                                  '<Question: tests past question 3?>',
                                  '<Question: tests past question 1?>'])


class QuestionDetailViewTest(TestCase):
    # the detail view of the question in future should return 404
    def test_detail_view_with_future_question(self):
        future_question = create_question("future question?", 1)
        response = self.client.get(reverse('polls:detail', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_past_question(self):
        past_question = create_question("past question?", -1)
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text, status_code=200)