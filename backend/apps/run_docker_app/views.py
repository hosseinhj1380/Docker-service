from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RunDockerSerializer
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .models import RunDockerModel,Logs
from apps.services.Run_Docker_app import run_docker


class RunDockerApp(CreateAPIView):
    serializer_class = RunDockerSerializer
    
    def create(self, request, *args, **kwargs):
        response = []

        # Loop through the data received in the request
        for data in request.data:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)

            # Run the Docker app using the utility function
            result = run_docker(parameters=serializer.validated_data)

            # Create a Logs instance with the result parameters and status
            logs = Logs.objects.create(
                parameters=result["parameters"],
                status=result["status"]
            )

            # Create a RunDockerModel instance with the provided data and logs
            instance = RunDockerModel(
                name=data.get("name"),
                image=data.get("image"),
                envs=data.get("envs"),
                command=data.get("command"),
                logs=logs
            )

            # Save the instance to the database
            instance.save()

            # Append the result message and error to the response list
            response.append({
                "message": result["message"],
                "error": result["error"]
            })

        # Return the response with a 201 CREATED status
        return Response(response, status=status.HTTP_201_CREATED)


    
