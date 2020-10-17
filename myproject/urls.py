"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static

from reports.views import home
from blog.views import blog_post_create
from Adminsite.views import Adminhome
from account.views import loginuser, logout_user
from policestation.views import policestation_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog-new/', blog_post_create ),
    path('policestation-new/', policestation_create),
    path('', include('reports.urls', namespace= 'reports')),
    path('', include('Adminsite.urls', namespace= 'Admin')),
    path('blog/', include('blog.urls', namespace= 'blog')),
    path('policestation/', include('policestation.urls', namespace= 'policestation')),
    path('login/', loginuser ),
    path('logout/', logout_user),
    

    path('', home, name= 'home'),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
