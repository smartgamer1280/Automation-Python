#views for app polls

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import Http404



def index(request):
    d = {"me": "Django", "dev": "development"}
    
   

    return render(request, 'polls/index.html', d)


def main(request):
    return render(request, 'polls/index2.html')


def social(request):
    return render(request, 'polls/index3.html')


def contact(request):
    return render(request, 'polls/index4.html')


def about(request):
    return render(request, 'polls/index5.html')


def Login(request):
    return render(request, 'polls/index6.html')
