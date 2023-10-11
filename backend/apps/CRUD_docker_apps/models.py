from django.db import models

# Create your models here.
class CreateDockerModel(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    image=models.CharField(null=False,blank=False,max_length=255)   
    envs=models.JSONField()
    command=models.CharField(null=True,blank=True, max_length=50)