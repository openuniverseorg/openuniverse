from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Thes views are python functions that take a request from the user request and return something.
# Most of the time the users are going to request the webpage, and we are going to return it.

def index(request):
    template = loader.get_template('mainpage/index.html')
    context = {} # Context are the values that I want to send to my HTML
    return HttpResponse(template.render(context, request))
