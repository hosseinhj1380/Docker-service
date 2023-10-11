from django.urls import path, include
from .views import run_docker_app



urlpatterns = [
    path('',run_docker_app)
]

