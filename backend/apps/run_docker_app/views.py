from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RunDockerSerializer
from rest_framework import status
from .models import RunDockerModel,Logs
from apps.services.Run_Docker_app import run_docker
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@api_view(['POST'])

def run_docker_app(request):
    if request.method=="POST":
        response=[]
        for data in request.data:
            print("asdasd")
            name = data.get("name")
            image = data.get("image")
            envs = data.get("envs")
            command = data.get("command")

            serializer=RunDockerSerializer(data=data)
            if serializer.is_valid():
                result=run_docker(parameters=serializer.validated_data)

                logs = Logs.objects.create(
                                            parameters=result["parameters"],
                                            status=result["status"])
                instance = RunDockerModel(
                                            name=name,
                                            image=image,
                                            envs=envs,
                                            command=command,
                                            logs=logs)
                                                        
                instance.save()
                response.append({"message":result["message"],
                                "error":result["error"]})
            else:
                break
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(response, status=status.HTTP_201_CREATED)
            

    
