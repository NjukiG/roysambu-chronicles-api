# from django.test import TestCase

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Articles

class RoysambuChroniclesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
        username="testuser",
        email="test@email.com",
        password="secret",
        )
        
        cls.article = Articles.objects.create(
        author=cls.user,
        title="A good title",
        subtitle="A good subtitle",
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1asV-lx5EDPkzs4B1-SBt6i16EkpfOzmlPHlLNEDkYnE6f24mVENZB4oPhrMMPCs2WWg&usqp=CAU",
        body="Nice body content",
        minutes_to_read= 5,
        )


    def test_post_model(self):
        self.assertEqual(self.article.author.username, "testuser")
        self.assertEqual(self.article.title, "A good title")
        self.assertEqual(self.article.subtitle, "A good subtitle")
        self.assertEqual(self.article.image, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1asV-lx5EDPkzs4B1-SBt6i16EkpfOzmlPHlLNEDkYnE6f24mVENZB4oPhrMMPCs2WWg&usqp=CAU")
        self.assertEqual(self.article.body, "Nice body content")
        self.assertEqual(self.article.minutes_to_read, 5)
        self.assertEqual(str(self.article), "A good title")

# Create your tests here.
