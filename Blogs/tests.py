from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from . import models as b_models



class BaseContentModelTest(TestCase):
    def test_is_recently_published_with_future_idea(self):
        """
        is_recently_published() returns False when pub_date of an Idea
        is in the future
        """
        future_time = timezone.now() + timedelta(days=5)
        idea_obj = b_models.Idea(pub_date=future_time)
        self.assertFalse(idea_obj.is_recently_published())

    def test_is_recently_published_with_past_idea(self):
        """
        is_recently_published() returns False when pub_date of an Idea
        is older than 5 days
        """
        past_time = timezone.now() - timedelta(days=8)
        idea_obj = b_models.Idea(pub_date=past_time)
        self.assertFalse(idea_obj.is_recently_published())


    def test_is_recently_published_with_recent_idea(self):
        """
        is_recently_published() returns True when pub_date of an Idea
        is within 5 days.
        """
        recent_time = timezone.now() - timedelta(days=2)
        idea_obj = b_models.Idea(pub_date=recent_time)
        self.assertIs(idea_obj.is_recently_published(), True)




class IdeaIndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
                username="testUser",
                email="testEmail@test.com",
                password="testPass@123",)

    def _create_idea(self, topic_text, days):
        idea_ob = b_models.Idea.objects.create(topic=topic_text,
                                   body="nothing",
                                   user=self.user
                                   )
        idea_ob.pub_date = timezone.now() + timedelta(days=days)
        idea_ob.save()
        return idea_ob

    def test_no_idea(self):
        """
        If Idea queryset is empty, Display an appropriate message
        """
        response = self.client.get(reverse("blogs:idea_index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Ideas are available.")
        self.assertQuerySetEqual(response.context["idea_list"], [])


    def test_past_idea(self):
        """
        Ideas with pub_date in past are displayed on the idea_index page
        """
        idea_ob = self._create_idea("-20days Idea", -20)
        response = self.client.get(reverse("blogs:idea_index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["idea_list"], [idea_ob])

    def test_multi_past_idea(self):
        """
        multiple Ideas must be displayes on idea_index page
        """
        idea_ob1 = self._create_idea("-20days Idea", -20)
        idea_ob2 = self._create_idea("-10days Idea", -10)
        response = self.client.get(reverse("blogs:idea_index"))
        self.assertQuerySetEqual(response.context["idea_list"], [idea_ob2, idea_ob1])

    def test_future_idea(self):
        """
        Ideas with pub_date in future are not displayed in idea_index page
        """
        idea_ob1 = self._create_idea("20days Idea", 20)
        response = self.client.get(reverse("blogs:idea_index"))
        self.assertQuerySetEqual(response.context["idea_list"], [])

    def test_future_idea_and_past_idea(self):
        """
        If both future and past published Ideas exist,
        Only past Ideas are displayed
        """
        idea_ob1 = self._create_idea("20days Idea", 20)
        idea_ob2 = self._create_idea("-10days Idea", -10)
        response = self.client.get(reverse("blogs:idea_index"))
        self.assertQuerySetEqual(response.context["idea_list"], [idea_ob2])



