from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'), 
    path('explore/', views.explore, name='explore'),
    path('search/', views.search, name='search'),
    path('<str:owner>/<str:name>', views.project, name='project')
    ]
