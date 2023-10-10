from django.urls import path, include
from .views import create_docker_app,docker_app_management



urlpatterns = [
    path('',create_docker_app),
    path('manage/<int:id>',docker_app_management)
]

