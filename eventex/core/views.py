# coding: utf-8
from django.views.generic.simple import direct_to_template

def homepage(request):
	return direct_to_template(request, template='index.html')


#1ª versão
#from django.http import HttpResponse
#from django.template import loader, Context

#def homepage(request):
#	t = loader.get_template('index.html')
#	c = Context()

#	content = t.render(c)

#	return HttpResponse(content)