from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from.serializers import CreateDockerSerializers
from .models import CreateDockerModel
from rest_framework.response import Response
from rest_framework import status
from apps.services.CRUDservices import create_docker_app,docker_app_lists
 
# Create your views here.
@api_view(["GET"])
def docker_app_list(request):
    
    return Response(docker_app_lists())



@api_view(["POST"])
def create_docker_app(request):

    serializer=CreateDockerSerializers(data=request.data)
    
    if serializer.is_valid():
        
        create_docker_app({
            "name":serializer.validated_data["name"],
            "image":serializer.validated_data["image"],
            "environment":serializer.validated_data["envs"],
            "command":serializer.validated_data["command"]
            })

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def docker_app_management(request,id):
    if request.method=="GET":
        docker_app=CreateDockerModel.objects.filter(id=id)
        print(docker_app)
        if docker_app :
            serializer=CreateDockerSerializers(docker_app,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response("dockerapp with this id is not found",status=status.HTTP_404_NOT_FOUND)

    elif request.method=="PUT":
        docker_app=CreateDockerModel.objects.filter(id=id)
        if docker_app:
            serializer=CreateDockerSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("dockerapp with this id is not found",status=status.HTTP_404_NOT_FOUND)
    elif request.method=="DELETE":
        try:
            docker_app = CreateDockerModel.objects.get(id=id)
            docker_app.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except docker_app.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)


