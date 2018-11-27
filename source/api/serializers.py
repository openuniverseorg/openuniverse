'''
	A Serializer transforms model instances into JSON. for API purposes
'''
# snippets/serializers
from rest_framework import serializers
from website.models import Project, ProjectFeatures, ProjectStatistics, TimeSeries

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'