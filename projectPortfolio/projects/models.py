from django.db import models


# Create your models here.
class Project(models.Model):
    objects = models.manager
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=250)
