from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView , ApiView
from.serializers import CreateDockerSerializers
from .models import CreateDockerModel
from rest_framework.response import Response
from rest_framework import status
from apps.services.CRUDservices import CRUDapp
from rest_framework.views import APIView
# Create your views here.

    

class DockerApp(ApiView):
    serializer_class = CreateDockerSerializers
    def post(self, request, *args, **kwargs):
        serializer=CreateDockerSerializers(data=request.data)
        if serializer.is_valid():
            obj = CRUDapp()
            result=obj.create_docker(parameters=
                {
                "name":serializer.validated_data["name"],
                "image":serializer.validated_data["image"],
                "envs":serializer.validated_data["envs"],
                "command":serializer.validated_data["command"]
                })

            serializer.save()
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        obj = CRUDapp()
        
        return Response(obj.docker_app_lists())


class DockerAppManagement(APIView):
    
    def get(self , request , *args , **kwargs):
        repository=self.kwargs.get("repository") 
        if repository:
            obj = CRUDapp()
            
            result=obj.docker_single_app_info(repository)
            
            return Response(result,status=status.HTTP_200_OK)
    def put(self , request , *args , **kwargs):
        obj = CRUDapp()
        
        delete_result=obj.delete_docker_app(repository=repository)

        if isinstance(delete_result,list):
            repository=self.kwargs.get("repository") 
            serializer=CreateDockerSerializers(data=request.data)

            if serializer.is_valid():
                create_result=obj.create_docker(parameters=
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
        
    def delete(self , request , *args , **kwargs):
        repository=self.kwargs.get("repository") 
        if repository: 
            obj = CRUDapp()
            

            result=obj.delete_docker_app(repository=repository)
            return Response(result,status=status.HTTP_200_OK)
        
