from django.shortcuts import render
from rest_framework import generics
from website.models import Project, ProjectStatistics, ProjectFeatures, TimeSeries
from .serializers import ProjectSerializer, ProjectStatisticsSerializer, ProjectFeaturesSerializer, TimeSeriesSerializer
#API root:
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
'''
ModelList method return single instances of a certain model, a read-only endpoint.
ModelDetail methods return single deatailed instances of a certain model, supporting CRUD API operations.

'''
#API root:
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'project': reverse('project-list', request=request, format=format),
        'project-statistics': reverse('project-statistics-list', request=request, format=format),
        'project-features': reverse('project-features-list', request=request, format=format),
        'time-series': reverse('time-series-list', request=request, format=format),
    })



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
