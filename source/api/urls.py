from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
	#Returning Project instances:
    path('project/', views.ProjectList.as_view()),
    path('project/<int:pk>/', views.ProjectDetail.as_view()),

    #Returning Project Statistics instances:
    path('project_statistics/', views.ProjectStatisticsList.as_view()),
    path('project_statistics/<int:pk>/', views.ProjectStatisticsDetail.as_view()),

    #Returning Project Features instances:
    path('project_features/', views.ProjectFeaturesList.as_view()),
    path('project_features/<int:pk>/', views.ProjectFeaturesDetail.as_view()),

    #Returning Project TimeSeries instances:
    path('time_series/', views.TimeSeriesList.as_view()),
    path('time_series/<int:pk>/', views.TimeSeriesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)