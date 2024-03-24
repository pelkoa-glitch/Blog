from django.test import TestCase


class TestBlog(TestCase):

    def test_blog(self):
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)
