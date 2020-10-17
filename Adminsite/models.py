from django.db import models

# Create your models here.


class PoliceStation(models.Model):
    name = models.CharField(max_length =50)
    location = models.CharField(max_length =50)
    Contacts = models.IntegerField()

    def __str__(self):
        return self.name

class News(models.Model):
    headline = models.CharField(max_length =50)
    Pub_date = models.DateField()
    reporter = models. CharField(max_length =50)
    content = models.CharField(max_length =10000)
    comments = models.CharField(max_length =1000)

    def __str__(self):
        return self.headline

class Wanted(models.Model):
    name = models.CharField(max_length=50)
    # id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='picture/', height_field=None, width_field=None, max_length=None)


    def  __str__(self):
        return self.name
class LostPerson(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='picture/', height_field=None, width_field=None, max_length=None)


    def __str__(self):
        return self.name

class Logindetails(models.Model):
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length =20)