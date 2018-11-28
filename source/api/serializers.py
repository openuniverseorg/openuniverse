'''
	A Serializer transforms model instances into JSON. for API purposes
'''
# snippets/serializers
from rest_framework import serializers
from website.models import Project, ProjectStatistics, ProjectFeatures, TimeSeries


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ProjectStatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectStatistics
        fields = '__all__'


class ProjectFeaturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectFeatures
        fields = '__all__'


class TimeSeriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeSeries
        fields = '__all__'
