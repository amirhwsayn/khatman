from uuid import uuid4

from django.db import models


# Create your models here.

class adminss(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid4())
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    namesc = models.CharField(max_length=50)
    number = models.CharField(max_length=11)

class classes(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid4())
    admin = models.ForeignKey(adminss , on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=10)


class stus(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid4())
    name = models.CharField(max_length=30)
    classstu = models.ForeignKey(classes , on_delete=models.CASCADE)
