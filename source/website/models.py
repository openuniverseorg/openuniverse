# -*- coding: utf-8 -*-
'''
    The models.py is responsible for defining the
    sources of information available in our database.
    Each class is a table, each variable is a column.
'''
from django.db import models

'''
    The Project model handles basic information of a project.
''' 
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

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

'''
    ProjectStatistics has some important metrics on a project
    It's linked by an on_to_one relation to the Project model
'''
class ProjectStatistics(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, primary_key=True)
    pulls_merged_total = models.IntegerField()
    newcomers_total = models.IntegerField()
    open_issues_total = models.IntegerField()
    used_languages_total = models.IntegerField()
    forks_total = models.IntegerField()
    stars_total = models.IntegerField()
    commits_total = models.IntegerField()
    contributors_total = models.IntegerField()
    core_members_total = models.IntegerField()

    class Meta:
        verbose_name_plural = "Projects Statistics"

    def __str__(self):
        return self.project

    def __unicode__(self):
        return self.project

'''
    Some features a projects repository might have
    It's linked by an on_to_one relation to the Project model
'''
class ProjectFeatures(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, primary_key=True)
    has_contributing = models.BooleanField()
    has_readme = models.BooleanField()

    class Meta:
        verbose_name_plural = "Projects Features"

    def __str__(self):
        return self.project

    def __unicode__(self):
        return self.project

'''
    A project's timeSeries tells much about what happened to the repository in a given day.
    It's largely used for charts construction and data analysis.
    It's linked by an on_to_one relation to the Project model
'''
class TimeSeries(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    data_type = models.TextField()
    count = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Projects Time Series"

    def __str__(self):
        return self.project

    def __unicode__(self):
        return self.project
