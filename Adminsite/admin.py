from django.contrib import admin

# Register your models here.

from .models import PoliceStation, News, Wanted, LostPerson


admin.site.register(PoliceStation)
admin.site.register(News)
admin.site.register(Wanted)
admin.site.register(LostPerson)
