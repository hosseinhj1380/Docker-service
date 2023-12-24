from django.urls import path, include
from .views import RunDockerApp



urlpatterns = [
    path('',RunDockerApp.as_view())
]

