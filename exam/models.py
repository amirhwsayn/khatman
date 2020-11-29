from django.db import models


# Create your models here.


class classes(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    datacreate = models.DateTimeField(auto_now=True)


class adminss(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    calsss = models.ManyToManyField(classes, blank=True)
    number = models.CharField(max_length=11)
    datacreate = models.DateTimeField(auto_now=True)


class stus(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    passwordstu = models.CharField(max_length=30, default=True)
    name = models.CharField(max_length=30)
    classthisstu = models.ManyToManyField(classes , blank=True)
    datacreate = models.DateTimeField(auto_now=True)

class imei_admin(models.Model):
    imei = models.CharField(primary_key=True , max_length=100)
    id_admin = models.CharField(max_length=100)
    pass_admin = models.CharField(max_length=100)

