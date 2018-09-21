from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'), 
    path('find/', views.find, name='find'),
    path('search/', views.search, name='search'),
    path('<str:owner>/<str:name>', views.project, name='project')
    ]
