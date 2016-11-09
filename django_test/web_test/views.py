from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    
    return HttpResponse('index')

def login(request):
    
    return HttpResponse('login')


def list(request,id,name):
    print(id,name)    
    return HttpResponse('list')