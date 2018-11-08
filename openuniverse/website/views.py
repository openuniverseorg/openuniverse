# -*- coding: utf-8 -*-
'''
    The views.py is responsible for handling with web requests
    and responses. The responses in our website
    usually are HTML pages containing data.
'''
from collections import Counter
from django.shortcuts import render, redirect
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
        'projects': Project.objects.values_list('name', flat=True),
        'licenses': Project.objects.values_list('software_license', flat=True).distinct(),
        'languages': Project.objects.values_list('main_language', flat=True).distinct(),
        'domains': Project.objects.values_list('application_domain', flat=True).distinct(),
        'projects_per_domain': dict(Counter(Project.objects.values_list('application_domain', flat=True))),
        'projects_per_age': dict(Counter(Project.objects.values_list('age', flat=True)))
        }

    return render(request, 'website/index.html', context)

def search(request):
    '''
        The search method is responsible for
        handling requests of the search field, defined in the navbar.
        When a request is done, the requested project is searched
        in the database.
    '''
    name = request.GET.get('name')

    try:
        requested_project = Project.objects.get(name=name)
        return redirect('website:project', owner=requested_project.owner, name=requested_project.name)
    except Project.DoesNotExist:
        raise Http404('Project does not exist')
    except Project.MultipleObjectsReturned:
        requested_project = Project.objects.get(name=name)[0]
        return redirect('website:project', owner=requested_project.owner, name=requested_project.name)

    return render(request, 'website:index.html')

def explore(request):
    '''
        The explore method is responsible for
        handling requests of the explore section, defined in the navbar.
        When a request is done, the parameters defined in the section
        are searched in the database. If no parameter is defined, all
        the projects are returned to the explore.html page.
        The values used in explore.html are transmitted
        using the context variable.
    '''

    languages = request.GET.getlist('language')
    domains = request.GET.getlist('domain')
    licenses = request.GET.getlist('license')
    selected_projects = Project.objects

    if languages:
        selected_projects = selected_projects.filter(main_language__in=languages)

    if domains:
        selected_projects = selected_projects.filter(application_domain__in=domains)

    if licenses:
        selected_projects = selected_projects.filter(software_license__in=licenses)

    context = {
        'projects': Project.objects.values_list('name', flat=True), 
        'licenses': Project.objects.values_list('software_license', flat=True).distinct(),
        'languages': Project.objects.values_list('main_language', flat=True).distinct(),
        'domains': Project.objects.values_list('application_domain', flat=True).distinct(),
        'selected_projects': selected_projects.values()
        }

    return render(request, 'website/explore.html', context)

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
            'project_features': ProjectStatistics.objects.get(project=requested_project.id),
            'projects': Project.objects.values_list('name', flat=True),
            'licenses': Project.objects.values_list('software_license', flat=True).distinct(),
            'languages': Project.objects.values_list('main_language', flat=True).distinct(),
            'domains': Project.objects.values_list('application_domain', flat=True).distinct()
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
