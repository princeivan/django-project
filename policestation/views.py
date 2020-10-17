from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import PoliceStation
from .forms import PoliceStationModelForm


def policestation_detail_view(request, slug):
    obj = get_object_or_404(PoliceStation, slug=slug)
    context = {'object':obj}

    return render(request,'policestation/detail.html', context)

def policestation_create(request):
    form = PoliceStationModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit =False)
        obj.user = request.user
        obj.save()
        form = PoliceStationModelForm()
    context = {"form":form}
    return render(request, 'policestation/form.html', context)

def policestation_list(request):
    qs= PoliceStation.objects.all()
    if request.user.is_authenticated:
        my_qs = PoliceStation.objects.filter(user=request.user)
        qs = (qs|my_qs)
    context = {"object_list":qs}
    return render(request, 'policestation/list.html',context)

    
def policestation_update(request, slug):
    obj = get_object_or_404(PoliceStation, slug=slug)
    form = PoliceStationModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context ={'form':form, "my_title":f"update{obj.name}"}
    return render(request, 'policestation/form.html', context)

def policestation_delete(request, slug):
    obj = get_object_or_404(PoliceStation, slug=slug)
    template_name = 'policestation/delete.html'
    if request.method =="POST":
        obj.delete()
        return redirect("/policestation")
    context = {'object':obj}
    return render(request, template_name, context)

