from django.db import models

# Create your models here.
class teacher(models.Model):
    Name = models.CharField(max_length=20)
    Identification = models.IntegerField()
    Contact = models.EmailField()
    Address = models.CharField(max_length=20)

class student(models.Model):
    Name = models.CharField(max_length=20)
    Identification = models.IntegerField()
    Contact = models.EmailField()
    Address = models.CharField(max_length=20)

class service_provider(models.Model):
    Name = models.CharField(max_length=20)
    Identification = models.IntegerField()
    Contact = models.EmailField()
    Address = models.CharField(max_length=20)
