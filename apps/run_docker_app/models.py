from django.db import models

# Create your models here.
class RunDockerModel(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    image=models.CharField(null=False,blank=False,max_length=255)   
    envs=models.JSONField()
    command=models.CharField(null=True,blank=True, max_length=50)
    logs=models.ForeignKey("Logs",on_delete=models.CASCADE,null=True, blank=True)

class Logs(models.Model):
    date = models.DateField(auto_now_add=True,verbose_name="date writed ")
    parameters=models.CharField(blank=False,null=False,max_length=255)