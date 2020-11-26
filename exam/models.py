from uuid import uuid4
from django.utils import timezone

from django.db import models


# Create your models here.

class adminss(models.Model):
    id = models.CharField(primary_key=True , max_length=30)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=11)
    datacreate = models.DateTimeField(auto_now=True)


class classes(models.Model):
    id = models.CharField(primary_key=True , max_length=30)
    admin = models.ForeignKey(adminss, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    datacreate = models.DateTimeField(auto_now=True)


class stus(models.Model):
    id = models.CharField(primary_key=True , max_length=30)
    name = models.CharField(max_length=30)
    classstu = models.ForeignKey(classes, on_delete=models.CASCADE)
    datacreate = models.DateTimeField(auto_now=True)
