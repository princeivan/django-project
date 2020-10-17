from django.contrib import admin

# Register your models here.

from reports.models import Report, Wanted, LostPerson


admin.site.register(Report)
admin.site.register(Wanted)
admin.site.register(LostPerson)
