# coding=utf-8

from django.test import TestCase
from django.test.client import Client
# from django.conf import settings
# from hike.models import Banner


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class TemplateContextTest(TestCase):
    def test_template_context(self):
        client = Client()
        response = client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['banner'], 'ERROR')


# class BannerTest(TestCase):
#     def setUp(self):
#         self.mountain = Banner.objects.create(image="Rock.jpg", text="Rock", state=0)
#         self.water = Banner.objects.create(image="Water.jpg", text="Water", state=1)

#     def test_banner(self):
#         self.mountain.state = 1
#         self.mountain.save()
#         print self.mountain.state
#         print self.water.state
#         self.assertEqual(self.water.state, 0)
#         self.assertEqual(self.mountain.state, 1)
