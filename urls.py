from django.contrib import admin
from django.urls import include, path
path(‘myApp/’, include(‘myApp.urls’)),
