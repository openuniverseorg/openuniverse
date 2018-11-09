from django.contrib import admin
from .models import Project, ProjectStatistics, ProjectFeatures, TimeSeries

admin.site.register(Project)
admin.site.register(ProjectStatistics)
admin.site.register(ProjectFeatures)
admin.site.register(TimeSeries)