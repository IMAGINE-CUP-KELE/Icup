from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def lp(request):
    return render(request,'web/index.html')

def home(request):
    return render(request,'web/home.html')

def wildflife(request):
    return render(request,'web/wildlife.html')

def forest(request):
    return render(request,'web/forest.html')

def visitors(request):
    return render(request,'web/visitors.html')

def logistics(request):
    return render(request, 'web/logistics.html')

