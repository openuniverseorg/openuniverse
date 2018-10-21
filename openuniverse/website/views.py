# Flake8 Pylint
from django.shortcuts import render, redirect
from django.db.models import F, Func, Value
from django.template import loader, RequestContext
from website.models import Projects
from django.http import Http404
from operator import itemgetter

#Auxiliar methods:
def index_bar_chart_helper():
	#This helper prepares the data for the fork chart
	#names:
	names = list(Projects.objects.all().values_list('name'))
	#total_forks:
	total_forks = [x['forks_total'] for x in list(Projects.objects.all().values_list('statistics'))]
	#result:
	liist = [[name,forks] for name,forks in zip(names,total_forks)]
	return sorted(liist, key=itemgetter(1))[-5:]

def index(request):
	context = {'projects': Projects.objects.values_list('name'), 
			   'licenses': Projects.objects.values_list('license').distinct('license'),
			   'languages': Projects.objects.values_list('main_language').distinct('main_language'),
			   'domains': Projects.objects.values_list('domain').distinct('domain'),
			   #This is used for the Domain chart
			   'domains_count' : list(Projects.objects.all().values_list('domain')),
			   #This is used for the Most Forked chart:
			   'most_forked' : index_bar_chart_helper(),
			   }

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

	context =  {'projects': Projects.objects.values_list('name'), 
				'licenses': Projects.objects.values_list('license').distinct('license'),
				'languages': Projects.objects.values_list('main_language').distinct('main_language'),
				'domains': Projects.objects.values_list('domain').distinct('domain'),
				'selected_projects': selected_projects.values_list('project_id', 'name', 'owner', 'license', 'statistics')}

	return render(request, 'website/find.html', context)
							
def project(request, owner, name):
	try:
		project = Projects.objects.get(name=name,owner=owner)
		context = {'project': project,
				   'projects': Projects.objects.values_list('name'),
				   'licenses': Projects.objects.values_list('license').distinct('license'),
				   'languages': Projects.objects.values_list('main_language').distinct('main_language'),
				   'domains': Projects.objects.values_list('domain').distinct('domain')}
		return render(request, 'website/project.html', context)
	except Projects.DoesNotExist:
		raise Http404('Project does not exist')
	except Projects.MultipleObjectsReturned:
		raise Http404('Project does not exist')

def handler404(request):
	return render(request, 'website/error404.html', status=404)
