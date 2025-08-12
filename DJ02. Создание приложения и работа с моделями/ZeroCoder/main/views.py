from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def data(request):
    return render(request, 'main/data.html')

def test(request):
    return render(request, 'main/test.html')



