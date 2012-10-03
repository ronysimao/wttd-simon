# coding: utf-8

from django import forms
from django.utils.translation import gettext as _
from eventex.subscriptions.models import Subscription

class SubscriptionForm(forms.Form):
	"""docstring for SubscriptionForm"""
	name = forms.CharField(label=_('Nome'))
	cpf = forms.CharField(label=_('CPF'))
	email = forms.CharField(label=_('Email'))
	phone = forms.CharField(label=_('Telefone'))
		
class SubscriptionForm(forms.ModelForm):
	#TODO: o que é uma classe meta ?
	class Meta:
		model = Subscription
		