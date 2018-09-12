# Here we have the url polls mapping
# Here is where we define the path that the user will request for polls app

from django.urls import path
from . import views

urlpatterns = [
    # If the user is requesting nothing more than just polls/, return index view
    path('index/', views.index, name='index'), 
    path('find/', views.find, name='find'),
    path('search/', views.search, name='search'),
    path('<str:owner>/<str:name>', views.project, name='project')
    ]
