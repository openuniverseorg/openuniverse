# Here we have the url general mapping
# Here is where we define the path that the user will request

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pages/', include('website.urls')),
    path('admin/', admin.site.urls),
]
