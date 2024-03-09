from django.db import models


# Create your models here.
class appModel(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=25)
    esal=models.CharField(max_length=25)
    ecity=models.CharField(max_length=25)
    econtact=models.CharField(max_length=25)
    edepart=models.CharField(max_length=25)
