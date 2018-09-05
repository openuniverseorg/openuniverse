from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from website.models import Projects

# Thes views are python functions that take a request from the user request and return something.
# Most of the time the users are going to request the webpage, and we are going to return it.

def index(request):
    template = loader.get_template('website/index.html')
    context = {'projects': Projects.objects.values_list('name'), 'licenses': Projects.objects.values_list('license').distinct('license'), 'languages': Projects.objects.values_list('main_language').distinct('main_language'), 'domains': Projects.objects.values_list('domain').distinct('domain')} # Context are the values that I want to send to my HTML
    return HttpResponse(template.render(context, request))
