#coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SucessTest(TestCase):
	"""docstring for SucessTest"""
	def setUp(self):		
		s = Subscription.objects.create(name='Rony Simao', cpf='12345678901', email='simao@rsimao.com.br',phone='11-980448533')
		self.resp = self.client.get('/inscricao/%d/' % s.pk)

	def test_get(self):
		'GET /inscricao/1/ should return status 200.'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		'Use template.'
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

	def test_context(self):
		'Context must have a subscription instance.'
		subscription = self.resp.context['subscription']
		self.assertIsInstance(subscription, Subscription)

	def test_html(self):
		'Check if subscription data was renderes.'
		self.assertContains(self.resp, 'Rony Simao')

class SucessNotFound(TestCase):
	"""docstring for SucessNotFound"""
	def test_not_found(self):
		response = self.client.get('/inscricao/0/')
		self.assertEqual(404, response.status_code)