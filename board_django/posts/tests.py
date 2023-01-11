import unittest

from django.test import TestCase
from django.urls import reverse
from .models import Post
from .views import HomePageView
from .apps import PostsConfig

# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='This is a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'This is a test')

class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='Some more')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

    def test_context_object_name(self):
        resp = HomePageView.context_object_name
        self.assertEqual(resp, 'all_posts_list')

class AppsTest(TestCase):

    def test_postsconfig_default(self):
        resp = PostsConfig.default_auto_field
        self.assertEqual(resp, 'django.db.models.BigAutoField')

    def test_db_name_default(self):
        resp = PostsConfig.name
        self.assertEqual(resp, 'posts')



