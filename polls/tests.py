import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        futureQuestion = Question(pub_date = time)
        self.assertIs(futureQuestion.was_published_recently(), False)

# Create your tests here.
