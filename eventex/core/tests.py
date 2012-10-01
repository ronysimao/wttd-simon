# coding: utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

#class HomepageTest(TestCase):
#	def test_get(self):
#		'GET / must return status code 200.'
#		response = self.client.get('/')
#		self.assertEquals(200, response.status_code)
#		self.assertTemplateUsed(response, 'index.html')
			