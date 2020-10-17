from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
User = settings.AUTH_USER_MODEL




class PoliceStation(models.Model):
    user = models.ForeignKey(User, default =1, null=True, on_delete = models.SET_NULL)
    name = models.CharField(max_length =50)
    slug =models.SlugField(unique = True, default = False)
    location = models.CharField(max_length =50)
    Contacts = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/policestation/{self.slug}/"

    def get_edit_url(self):
        return f"/policestation/{self.slug}/edit"

    def get_delete_url(self):
        return f"/policestation/{self.slug}/delete"
