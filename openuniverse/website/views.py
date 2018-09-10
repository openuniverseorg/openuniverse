from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext
from website.models import Projects
from django.http import Http404

# Thes views are python functions that take a request from the user request and return something.
# Most of the time the users are going to request the webpage, and we are going to return it.

def index(request):
    context = {'projects': Projects.objects.values_list('name'), 
               'licenses': Projects.objects.values_list('license').distinct('license'),
               'languages': Projects.objects.values_list('main_language').distinct('main_language'),
               'domains': Projects.objects.values_list('domain').distinct('domain')}

    return render(request, 'website/index.html', context)

def find(request):
    selected_languages = request.POST.getlist('language')
    selected_domains = request.POST.getlist('domain')
    selected_licenses = request.POST.getlist('license')
    selected_projects = Projects.objects

    if len(selected_languages) > 0:
        selected_projects = selected_projects(main_language__in=selected_languages)

    if len(selected_domains) > 0:
        selected_projects = selected_projects(domain__in=selected_domains)
    
    if len(selected_licenses) > 0:
        selected_projects = selected_projects(license__in=selected_licenses)

    context =  {'projects': Projects.objects.values_list('name'), 
                'licenses': Projects.objects.values_list('license').distinct('license'),
                'languages': Projects.objects.values_list('main_language').distinct('main_language'),
                'domains': Projects.objects.values_list('domain').distinct('domain'),
                'selected_projects': selected_projects, 
                'selected_languages': selected_languages,
                'selected_domains': selected_domains,
                'selected_licenses': selected_licenses}

    return render(request, 'website/find.html', context)
                            
def project(request, owner, name):
    try:
        project = Projects.objects.get(name=name,owner=owner)
        context = {'project': project}    
        return render(request, 'website/project.html', context)
    except Exception as e:
        if e.__class__.__name__ == 'DoesNotExist':
            raise Http404("Project does not exist")
        if e.__class__.__name__ == 'MultipleObjectsReturned':
            project = Projects.objects(name=name,owner=owner)[0]
            context = {'project': project}    
            return render(request, 'website/project.html', context)

def handler404(request):
    return render(request, 'website/error404.html', status=404)
    