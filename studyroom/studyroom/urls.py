from django.contrib import admin
from django.urls import path, include


# Use the base app urls for path to the app domain.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
