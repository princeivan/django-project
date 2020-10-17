from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

from .models import BLogpost
from .forms import BlogPostModelForm

def blog_post_detail(request,slug):
    obj = get_object_or_404(BLogpost, slug=slug)
    context ={"object":obj}
    return render(request, 'blog/detail.html', context)

def blog_post_create(request):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit =False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    context = {"form":form}
    return render(request, 'blog/form.html', context)

def blog_post_list(request):
    qs= BLogpost.objects.all()
    if request.user.is_authenticated:
        my_qs = BLogpost.objects.filter(user=request.user)
        qs = (qs|my_qs).distinct()
    context = {"object_list":qs}
    return render(request, 'blog/list.html',context)

    
def blog_post_update(request, slug):
    obj = get_object_or_404(BLogpost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context ={'form':form, "my_title":f"update{obj.title}"}
    return render(request, 'blog/form.html', context)

def blog_post_delete(request, slug):
    obj = get_object_or_404(BLogpost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method =="POST":
        obj.delete()
        return redirect("/blog")
    context = {'object':obj}
    return render(request, template_name, context)




