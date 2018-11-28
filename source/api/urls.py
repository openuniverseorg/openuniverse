from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

urlpatterns = [
    # Root:

    # Returning Project instances:
    path('project/', views.ProjectList.as_view(), name='project-list'),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),

    # Returning Project Statistics instances:
    path('project_statistics/', views.ProjectStatisticsList.as_view(),
         name='project-statistics-list'),
    path('project_statistics/<int:pk>/',
         views.ProjectStatisticsDetail.as_view(), name='project-statistics-detail'),

    # Returning Project Features instances:
    path('project_features/', views.ProjectFeaturesList.as_view(),
         name='project-features-list'),
    path('project_features/<int:pk>/',
         views.ProjectFeaturesDetail.as_view(), name='project-features-detail'),

    # Returning Project TimeSeries instances:
    path('time_series/', views.TimeSeriesList.as_view(), name='time-series-list'),
    path('time_series/<int:pk>/', views.TimeSeriesDetail.as_view(),
         name='time-series-detail'),
    # Root:
    path('', views.api_root)

]

urlpatterns = format_suffix_patterns(urlpatterns)

'''
# Returning Project Statistics instances:

'''
