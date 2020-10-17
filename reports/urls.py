from django.urls import path

from . import views

app_name = 'reports'
urlpatterns = [

    path('reports', views.reports, name ='reports'),
    path('news', views.news, name ='news'),
    path('policestation', views.police_stations, name ='policestation'),
    path('wanted', views.wantedpersons, name ='wanted'),
    path('Lostperson', views.lost_person, name ='lostperson'),
    
  
]