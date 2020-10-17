
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def loginuser(request):
    if request.method =="POST":
        username = request.POST. get('username')
        password = request.POST.get('password')
        user = authenticate(request, username =username, password =password)
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'Admin:Adminhome')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Bad username or password')
    return render(request, 'account/login.html', {})
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
