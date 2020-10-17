from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
User = settings.AUTH_USER_MODEL

class BLogpost(models.Model):
    user = models.ForeignKey(User, default =1, null=True, on_delete = models.SET_NULL)
    title = models.CharField(max_length =50)
    image =models.ImageField(upload_to = 'pictures/', blank= True, null =True)
    slug = models.SlugField(unique=True)
    publication_date =models.DateTimeField(auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    Reporter =models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    comments = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"

    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"

    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"

    

