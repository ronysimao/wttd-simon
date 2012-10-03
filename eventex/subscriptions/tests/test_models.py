# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Rony Simao',
			cpf='12345678901',
			email='simao@rsimao.com.br',
			#TODO: pode haver um problema aqui, pois coloquei o nono dígito
			phone='11-980448533'
		)

	def test_create(self):
		'Subscription must have name, cpf, email and phone.'
		self.obj.save()
		self.assertEqual(1, self.obj.id)

	def test_has_created_at(self):
		'Subscription must have automatic created_at'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_unicode(self):
		self.assertEqual(u'Rony Simao', unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
	def setUp(self):
		#Create a first entry to force the collision
		Subscription.objects.create(name='Rony Simao', cpf='12345678901', email='simao@rsimao.com.br', phone='11-980448533')

	def test_cpf_unique(self):
		'CPF must be unique'
		s = Subscription(name='Rony Simao', cpf='12345678901', email='simao@rsimao.com.br', phone='11-980448533')
		self.assertRaises(IntegrityError, s.save)

	def test_email_unique(self):
		'email must be unique'
		s = Subscription(name='Rony Simao', cpf='12345678901', email='simao@rsimao.com.br', phone='11-980448533')
		self.assertRaises(IntegrityError, s.save)
