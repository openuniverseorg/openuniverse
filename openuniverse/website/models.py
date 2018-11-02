from django.db import models

class Project(models.Model): 
    name = models.TextField()
    owner = models.TextField()
    owner_type = models.TextField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    application_domain = models.TextField()
    software_license = models.TextField()
    age = models.IntegerField()
    main_language = models.TextField()
    github_url = models.TextField()

class ProjectStatistics(models.Model):
    project = models.OneToOneField(Project, on_delete = models.CASCADE, primary_key = True)
    pulls_merged_total = models.IntegerField()
    newcomers_total = models.IntegerField()
    open_issues_total = models.IntegerField()
    used_languages_total = models.IntegerField()
    forks_total = models.IntegerField()
    stars_total = models.IntegerField()
    commits_total = models.IntegerField()
    contributors_total = models.IntegerField()
    core_members_total = models.IntegerField()

class ProjectFeatures(models.Model):
    project = models.OneToOneField(Project, on_delete = models.CASCADE, primary_key = True)
    has_contributing = models.BooleanField()
    has_readme = models.BooleanField()
    has_wiki = models.BooleanField()

class TimeSeries(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    count = models.IntegerField()
    date = models.DateTimeField()
