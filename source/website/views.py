# -*- coding: utf-8 -*-
'''
    The views.py is responsible for handling with web requests
    and responses. The responses in our website
    usually are HTML pages containing data.
'''
from collections import Counter, OrderedDict
from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404
from website.models import Project, ProjectStatistics, ProjectFeatures, TimeSeries

def index(request):
    '''
        The index method is responsible for
        handling index page requests.
        The values used in index.html are transmitted
        using the context variable.
    '''
    context = {
        'licenses': Project.objects.values_list('software_license', flat=True).distinct(),
        'languages': Project.objects.values_list('main_language', flat=True).distinct(),
        'domains': Project.objects.values_list('application_domain', flat=True).distinct(),
        }

    return render(request, 'website/index.html', context)

def explore(request):
    context = {}
    return render(request, 'website/explore.html', context)

def overview(request):
    context = {
        'projects_per_domain': OrderedDict(Counter(Project.objects.values_list('application_domain', flat=True)).most_common()),
        'projects_per_license': OrderedDict(Counter(Project.objects.values_list('software_license', flat=True)).most_common()),
        'projects_per_age': dict(Counter(Project.objects.values_list('age', flat=True)))
        }

    return render(request, 'website/overview.html', context)

def search(request):
    '''
        The search method is responsible for
        handling requests of the search field and the explore section.
        When a request is done, the requested parameters are filtered
        in the database.
    '''
    page = request.GET.get('page')
    query = request.GET.get('query')
    languages = request.GET.getlist('language')
    domains = request.GET.getlist('domain')
    licenses = request.GET.getlist('license')
    projects = Project.objects.all()

    if query:
        projects = projects.filter(name__contains=query)
    
    if languages:
        projects = projects.filter(main_language__in=languages)

    if domains:
        projects = projects.filter(application_domain__in=domains)

    if licenses:
        projects = projects.filter(software_license__in=licenses)

    paginator = Paginator(projects, 10)
    projects_list = paginator.get_page(page)

    context = {
        'projects_list': projects_list
        }

    return render(request, 'website/search.html', context)

def project(request, owner, name):
    '''
        The project method is responsible for
        handling projects requests. The values used in
        project.html are transmitted using the context variable.
    '''
    try:
        requested_project = Project.objects.get(name=name, owner=owner)

        context = {
            'project': requested_project,
            'newcomers_time_series': TimeSeries.objects.filter(project=requested_project.id, data_type='newcomers'),
            'project_statistics': ProjectStatistics.objects.get(project=requested_project.id),
            'project_features': ProjectStatistics.objects.get(project=requested_project.id)
            }
        return render(request, 'website/project.html', context)
    except Project.DoesNotExist:
        raise Http404('Project does not exist')
    except Project.MultipleObjectsReturned:
        raise Http404('Project does not exist')

def handler404(request):
    '''
        The handler404 method is responsible for
        handling exceptions. A clear example
        is the "DoesNotExist" exception.
    '''
    return render(request, 'website/error404.html', status=404)
