from django.shortcuts import render
from rest_framework import generics
from website.models import Project, ProjectStatistics, ProjectFeatures, TimeSeries
from .serializers import ProjectSerializer, ProjectStatisticsSerializer, ProjectFeaturesSerializer, TimeSeriesSerializer

'''
ModelList method return single instances of a certain model, a read-only endpoint.
ModelDetail methods return single deatailed instances of a certain model, supporting CRUD API operations.

'''
# This variable sets read-only permission to not authenticated users to
# all endpoints


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectStatisticsList(generics.ListCreateAPIView):
    queryset = ProjectStatistics.objects.all()
    serializer_class = ProjectStatisticsSerializer


class ProjectStatisticsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectStatistics.objects.all()
    serializer_class = ProjectStatisticsSerializer


class ProjectFeaturesList(generics.ListCreateAPIView):
    queryset = ProjectFeatures.objects.all()
    serializer_class = ProjectFeaturesSerializer


class ProjectFeaturesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectFeatures.objects.all()
    serializer_class = ProjectFeaturesSerializer


class TimeSeriesList(generics.ListCreateAPIView):
    queryset = TimeSeries.objects.all()
    serializer_class = TimeSeriesSerializer


class TimeSeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeSeries.objects.all()
    serializer_class = TimeSeriesSerializer
