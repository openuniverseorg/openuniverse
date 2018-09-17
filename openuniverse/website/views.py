# Flake8 Pylint
from django.shortcuts import render, redirect
from django.db.models import F, Func, Value
from django.template import loader, RequestContext
from website.models import Projects
from django.http import Http404

def index(request):
	context = {'projects': Projects.objects, 
			   'licenses': Projects.objects.values_list('license').distinct('license'),
			   'languages': Projects.objects.values_list('main_language').distinct('main_language'),
			   'domains': Projects.objects.values_list('domain').distinct('domain')}

	return render(request, 'website/index.html', context)

def search(request):
	name = request.GET.get('name')

	try:
		project = Projects.objects.get(name=name)
		return redirect('website:project', owner=project.owner, name=project.name)
	except Projects.DoesNotExist:
		raise Http404('Project does not exist')
	except Projects.MultipleObjectsReturned:
		project = Projects.objects.get(name=name)[0]
		return redirect('website:project', owner=project.owner, name=project.name)

	return render(request, 'website:index.html')
	
def find(request):
	selected_languages = request.GET.getlist('language')
	selected_domains = request.GET.getlist('domain')
	selected_licenses = request.GET.getlist('license')
	selected_projects = Projects.objects

	if len(selected_languages) > 0:
		selected_projects = selected_projects(main_language__in=selected_languages)

	if len(selected_domains) > 0:
		selected_projects = selected_projects(domain__in=selected_domains)
	
	if len(selected_licenses) > 0:
		selected_projects = selected_projects(license__in=selected_licenses)

	context =  {'projects': Projects.objects, 
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
		context = {'project': project,
				   'projects': Projects.objects, 
				   'licenses': Projects.objects.values_list('license').distinct('license'),
				   'languages': Projects.objects.values_list('main_language').distinct('main_language'),
				   'domains': Projects.objects.values_list('domain').distinct('domain')}

		return render(request, 'website/project.html', context)
	except Projects.DoesNotExist:
		raise Http404('Project does not exist')
	except Projects.MultipleObjectsReturned:
		project = Projects.objects(name=name,owner=owner)[0]
		context = {'project': project,
					'projects': Projects.objects, 
					'licenses': Projects.objects.values_list('license').distinct('license'),
					'languages': Projects.objects.values_list('main_language').distinct('main_language'),
					'domains': Projects.objects.values_list('domain').distinct('domain')}

		return render(request, 'website/project.html', context)

def handler404(request):
	return render(request, 'website/error404.html', status=404)
