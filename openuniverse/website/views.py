from django.shortcuts import render, redirect
from website.models import Project
from django.http import Http404

def index(request):
	context = {'projects': Project.objects.values_list('name', flat=True), 
			   'licenses': Project.objects.values_list('software_license', flat=True).distinct(),
			   'languages': Project.objects.values_list('main_language', flat=True).distinct(),
			   'domains': Project.objects.values_list('application_domain', flat=True).distinct()}
	return render(request, 'website/index.html', context)

def search(request):
	name = request.GET.get('name')

	try:
		project = Project.objects.get(name=name)
		return redirect('website:project', owner=project.owner, name=project.name)
	except Project.DoesNotExist:
		raise Http404('Project does not exist')
	except Project.MultipleObjectsReturned:
		project = Project.objects.get(name=name)[0]
		return redirect('website:project', owner=project.owner, name=project.name)

	return render(request, 'website:index.html')
	
def find(request):
	languages = request.GET.getlist('language')
	domains = request.GET.getlist('domain')
	licenses = request.GET.getlist('license')
	selected_projects = Project.objects

	if len(languages) > 0:
		selected_projects = selected_projects.filter(main_language__in=languages)

	if len(domains) > 0:
		selected_projects = selected_projects.filter(application_domain__in=domains)
	
	if len(licenses) > 0:
		selected_projects = selected_projects.filter(software_license__in=licenses)

	context =  {'projects': Project.objects.values_list('name', flat=True), 
				'licenses': Project.objects.values_list('software_license', flat=True).distinct(),
				'languages': Project.objects.values_list('main_language', flat=True).distinct(),
				'domains': Project.objects.values_list('application_domain', flat=True).distinct(),
				'selected_projects': selected_projects.values_list('id', 'name', 'owner', 'software_license')}

	return render(request, 'website/find.html', context)
							
def project(request, owner, name):
	try:
		requested_project = Project.objects.get(name=name,owner=owner)
		context = {'project': project,
				   'projects': Project.objects.values_list('name', flat=True),
				   'licenses': Project.objects.values_list('software_license', flat=True).distinct(),
				   'languages': Project.objects.values_list('main_language', flat=True).distinct(),
				   'domains': Project.objects.values_list('application_domain', flat=True).distinct()}
		return render(request, 'website/project.html', context)
	except Project.DoesNotExist:
		raise Http404('Project does not exist')
	except Project.MultipleObjectsReturned:
		raise Http404('Project does not exist')

def handler404(request):
	return render(request, 'website/error404.html', status=404)
