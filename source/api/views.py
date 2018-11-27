from django.shortcuts import render
from rest_framework import generics
from website.models import Project, ProjectStatistics, TimeSeries
from .serializers import ProjectSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer	
