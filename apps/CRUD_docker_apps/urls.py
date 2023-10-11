from django.urls import path, include
from .views import create_docker_app,docker_app_management,docker_app_list



urlpatterns = [
    path('docker-app-list',docker_app_list),
    path('create-app',create_docker_app),
    path('manage/<str:repository>',docker_app_management)
]

