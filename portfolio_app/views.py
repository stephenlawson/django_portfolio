from contextlib import redirect_stderr
from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from tenacity import retry

from .filters import PhotoFilter
from .forms import ContactForm, PhotoForm
from django.contrib import messages
import os
from django.conf import settings
from .models import Category, Photo, Project, PhotoIndex, PortfolioIndex
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def error_404_view(request, exception):
    return render(request, 'errors/404.html')

def error_500_view(request):
    return render(request, 'errors/500.html')

def error_403_view(request, exception):
    return render(request, 'errors/403.html')

def error_400_view(request, exception):
    return render(request, 'errors/400.html')

def home(request):
    projects = Project.objects.filter(active=True)
    about = PortfolioIndex.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Thank you for your inquiry, {name}')
            return redirect('/portfolio')
        else:
            messages.warning(request, f'Form was not valid.')
    else:
        form = ContactForm()
    context = {'form':form, 'projects':projects, 'about': about}
    return render(request, 'portfolio_app/index.html', context)

def projects(request):
	projects = Project.objects.filter(active=True)
	context = {'projects':projects}
	return render(request, 'portfolio_app/projects.html', context)

def project(request, slug):
    projects = Project.objects.filter(active=True).exclude(slug=slug)
    project = Project.objects.get(slug=slug)
    context = {'project':project, 'projects':projects}
    return render(request, 'portfolio_app/project.html', context)


def photography(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Thank you for your inquiry, {name}')
            return redirect('/')
        else:
            messages.warning(request, f'Form was not valid.')
    else:
        form = PhotoForm()
    context = {'form':form}
    return render(request, 'portfolio_app/photo_index.html', context)

def gallery(request):
    photos = Photo.objects.all()
    #categories =Category.objects.all()
    myFilter = PhotoFilter(request.GET, queryset=photos)
    photos = myFilter.qs
    

    page = request.GET.get('page')
    paginator =Paginator(photos, 9)
    try: 
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    context = { 'photos':photos, 'myFilter': myFilter}
    return render(request, 'portfolio_app/gallery.html', context)



def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'portfolio_app/photo.html', {'photo':photo})

def PrivacyPolicy(request):
    return render(request, 'portfolio_app/privacy_policy.html')