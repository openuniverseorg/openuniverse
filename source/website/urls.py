from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'), 
    path('search', views.search, name='search'),
    path('explore', views.explore, name='explore'),
    path('overview', views.overview, name='overview'),
    path('<str:owner>/<str:name>', views.project, name='project')
    ]
