import unittest

from django.test import TestCase
from .models import Post
from .views import HomePageView
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='This is a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'This is a test')

class testViews(unittest.TestCase()):
    def test_homepage(self):
        result = HomePageView.template_name
        self.assertEqual(result,'home.html')
