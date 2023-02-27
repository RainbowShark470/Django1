from django.test import TestCase
from .models import Blog


# Create your tests here.

class BlogTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(title="Test blog", description="This is a test blog.", owner="Test owner")

    def test_blog_has_owner(self):
        blog = Blog.objects.get(title="Test blog")
        self.assertEqual(blog.owner, "Test owner")
