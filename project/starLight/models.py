from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    date =  models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name