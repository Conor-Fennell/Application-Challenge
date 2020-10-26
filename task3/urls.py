from django.urls import path
from . import views  #import our views file from the current directory


urlpatterns = [
    #get sent to here from the main urls.py file
    #when we receive an empty string, we run the views.home function
    path('', views.home, name='task3-home'),
]