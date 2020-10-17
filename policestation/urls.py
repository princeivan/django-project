from django.urls import path

from . import views

app_name = 'policestation'

urlpatterns =[
    path('', views.policestation_list ),
    path('<str:slug>/', views.policestation_detail_view ),
    path('<str:slug>/edit', views.policestation_update ),
    path('<str:slug>/delete/', views.policestation_delete ),

]