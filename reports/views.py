import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.

from .forms import ReportForm
from .models import Report
from  Adminsite.models import PoliceStation, News, Wanted, LostPerson



def home(request):
    return render(request, 'index.htm')


def reports(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your Report was successfully send.')
            return redirect('reports:reports')

    else:
        form = ReportForm()
    context = {'form':form}

    return render(request, 'reports/reports.html', context)

def news(request):
    query_results = News.objects.all()
    context ={
        'query_results':query_results
    }
    return render(request, 'reports/news.html', context)


def police_stations(request):
    query_results = PoliceStation.objects.all()
    context ={
        'query_results':query_results
    }
    return render(request, 'reports/policestation.html', context)


def wantedpersons(request):
    theresults = Wanted.objects.all()
    context ={
        'theresults':theresults
    }
    
    return render(request, 'reports/wantedperson.html', context)


def lost_person(request):
    theresults = LostPerson.objects.all()
    context ={
        'theresults':theresults
    }
    return render(request, 'reports/lostperson.html', context)
    