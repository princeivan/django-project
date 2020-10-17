from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


from .models import PoliceStation,News, Wanted, LostPerson, Logindetails
from .forms import ReportForm, Police_Station, NewsForm, WantedForm, LostPersonForm

from reports.models import Report
 
@login_required
def Adminhome(request):
    return render(request, 'Adminsite/index.html')


# def loginuser(request):
#     if request.method =="POST":
#         username = request.POST. get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username =username, password =password)
#         if user is not None:
#             login(request, user)
#             redirect_url = request.GET.get('next', 'Admin:Adminhome')
#             return redirect(redirect_url)
#         else:
#             messages.error(request, 'Bad username or password')
#     return render(request, 'Adminsite/login.html', {})
# @login_required
# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('home'))

@login_required
def reports(request):
    query_results = Report.objects.all()
    context ={
        'query_results':query_results
    }
    
    return render(request, 'Adminsite/reports.html', context)
@login_required    
def Add_reports(request):
    if request.method =='POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Report Added succesfully')
    else:
        form = ReportForm()
    context = {'form':form}
    return render(request, 'Adminsite/Addreport.html', context)
@login_required
def news_views(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Police Station successfully added!")
    else:
        form = NewsForm()
    context = {'form':form}

    return render(request, 'Adminsite/news.html', context)

@login_required
def police_stations(request):
    if request.method == 'POST':
        form = Police_Station(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Police Station successfully added!",
            extra_tags="alert alert-success")
    else:
        form = Police_Station()
    context = {'form':form}
    return render(request, 'Adminsite/policestation.html', context)
@login_required
def viewpolicestation(request):
    theresults = PoliceStation.objects.all()
    context ={
        'theresults':theresults
    }
    
    return render(request, 'Adminsite/viewpolicestation.html', context)


@login_required
def wanted_person(request):
    if request.method == 'POST':
        form = WantedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Police Station successfully added!",
            extra_tags="alert alert-success")
    else:
        form = WantedForm()
    context = {'form':form}
    return render(request, 'Adminsite/wanted_person.html', context)
    
def viewwanted_person(request):
    theresults = Wanted.objects.all()
    context ={
        'theresults':theresults
    }
    
    return render(request, 'Adminsite/viewWanted_list.html', context)

@login_required
def lost_person(request):
    if request.method == 'POST':
        form = LostPersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Police Station successfully added!",
            extra_tags="alert alert-success")
    else:
        form = LostPersonForm()
    context = {'form':form}
    return render(request, 'Adminsite/lostperson.html', context)