from .models import CreateDockerModel
from rest_framework.serializers import ModelSerializer

class CreateDockerSerializers(ModelSerializer):
    class Meta:
        model=CreateDockerModel
        fields="__all__"