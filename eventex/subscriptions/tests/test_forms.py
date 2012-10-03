# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

'Mova o teste SubscribeTest.test_form_has_fields para o test_forms.py'

class SubscriptionFormTest(TestCase):

	def test_form_has_fields(self):
		'Form must have 4 fields.'
		form = SubscriptionForm()
		self.assertItemsEqual(['name','email','cpf','phone'], form.fields)