from django.urls import path

from . import views

app_name = 'Admin'

urlpatterns = [
   path('Adminhome', views.Adminhome, name ='Adminhome'),
   path('Adminreports', views.reports, name='Adminreports'),
   path('Addreport',views.Add_reports, name='Addreport'),
   path('Adminnews', views.news_views, name='Adminnews'),
   path('viewwanted', views.viewwanted_person, name= 'viewwanted'),
   path('viewpolicestation', views.viewpolicestation, name= 'viewpolicestation'),
   path('Adminpolicestaton', views.police_stations, name= 'Adminpolicestation'),
   path('Adminwanted', views.wanted_person, name='Adminwanted'),
   path('Adminlostperson', views.lost_person, name ='Adminlostperson'),
   # path('login', views.loginuser, name = 'login'),
   # path('logout', views.logout_user, name = 'logout')

   
]