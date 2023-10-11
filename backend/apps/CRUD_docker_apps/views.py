from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from.serializers import CreateDockerSerializers
from .models import CreateDockerModel
from rest_framework.response import Response
from rest_framework import status
from apps.services.CRUDservices import create_docker,docker_app_lists,docker_single_app_info,delete_docker_app
 
# Create your views here.
@api_view(["GET"])
def docker_app_list(request):
    
    return Response(docker_app_lists())



@api_view(["POST"])
def create_docker_app(request):
    if request.method=="POST":

        serializer=CreateDockerSerializers(data=request.data)
        
        if serializer.is_valid():
            

            
            result=create_docker(parameters=
                {
                "name":serializer.validated_data["name"],
                "image":serializer.validated_data["image"],
                "envs":serializer.validated_data["envs"],
                "command":serializer.validated_data["command"]
                })

            serializer.save()
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def docker_app_management(request,repository):
    if request.method=="GET":

        if repository :
            result=docker_single_app_info(repository)
            
            return Response(result,status=status.HTTP_200_OK)


    elif request.method=="PUT":
        delete_result=delete_docker_app(repository=repository)

        if isinstance(delete_result,list):
            serializer=CreateDockerSerializers(data=request.data)

            if serializer.is_valid():
                create_result=create_docker(parameters=
                {
                "name":serializer.validated_data["name"],
                "image":serializer.validated_data["image"],
                "envs":serializer.validated_data["envs"],
                "command":serializer.validated_data["command"]
                })
                serializer.save()
                return Response(create_result)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("dockerapp with this repository is not found",status=status.HTTP_404_NOT_FOUND)

            
    elif request.method=="DELETE":

        if repository: 

            result=delete_docker_app(repository=repository)
            return Response(result,status=status.HTTP_200_OK)
        


