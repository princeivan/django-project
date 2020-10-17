from django.db import models

# Create your models here.

class Report(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    Time = models.TimeField(auto_now=False, auto_now_add=False)
    Date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)


    def  __str__(self):
        return self.title

class Wanted(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key= True)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)


    def  __str__(self):
        return self.name
class LostPerson(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key= True)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)


    def __str__(self):
        return self.name



