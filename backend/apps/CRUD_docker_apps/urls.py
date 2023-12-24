from django.urls import path, include
from .views import create_docker_app,docker_app_management,DockerApp



urlpatterns = [
    path('docker-app-list',DockerApp.as_view()),
    path('create-app',DockerApp.as_view()),
    path('manage/<str:repository>',docker_app_management)
]

