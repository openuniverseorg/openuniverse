# Here we have the url general mapping
# Here is where we define the path that the user will request

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # url user is requesting: 'polls/', what django will return: something in polls/urls.py
    path('website/', include('website.urls')),
    # url user is requesting: 'admin/', what django will return: admin.site.urls
    path('admin/', admin.site.urls),
]
