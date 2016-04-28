# coding=utf-8

from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
import sys
import StringIO
from django.db.models import get_models


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class BlogTest(TestCase):
    fixtures = ['initial_data.json', 'blog']

    def test_user(self):
        person = CustomUser.objects.get(pk=1)
        self.assertEqual(person.user.is_superuser, True)
        self.assertIsNotNone(person.user.username)

    def test_profile_page(self):
        """
        Test for open main page
        """
        client = Client()
        person = CustomUser.objects.get(pk=1)
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<!DOCTYPE html>')
        self.assertContains(response, person.user.email)
        self.assertTemplateUsed(response, 'index.html')


# class MiddlewareTest(TestCase):
#     def test_request_page(self):
#         client = Client()
#         response = client.get('/request_page/creation_date')
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, '<!DOCTYPE html>')
#         self.assertTemplateUsed(response, 'request_page.html')

#     def test_middleware(self):
#         client = Client()
#         response = client.get('/')
#         log_entry = RequestPath.objects.get(path='/')
#         self.assertNotEquals(log_entry, None)


# class TemplateContextTest(TestCase):
#     def test_template_context(self):
#         client = Client()
#         response = client.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.context['my_settings'], settings)
