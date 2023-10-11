from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RunDockerSerializer
from rest_framework import status
from .models import RunDockerModel

@api_view(['POST',"GET"])
def run_docker_app(request):
    if request.method=="GET":
        docker_run=RunDockerModel.objects.all()
        serializer=RunDockerSerializer(docker_run, many=True)
        return Response(serializer.data)
    
    elif request.method=="POST":
        serializer=RunDockerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
