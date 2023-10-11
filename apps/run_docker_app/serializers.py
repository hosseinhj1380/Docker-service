from rest_framework.serializers import ModelSerializer
from .models import RunDockerModel

class RunDockerSerializer (ModelSerializer):
    class Meta:
        model=RunDockerModel
        fields=["name","image","envs","command"]
    
