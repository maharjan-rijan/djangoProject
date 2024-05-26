from django.db import models
class Service(models.Model):
    service_icon=models.CharField(max_length=80)
    service_title=models.CharField(max_length=80)
    service_des=models.TextField()
# Create your models here.
