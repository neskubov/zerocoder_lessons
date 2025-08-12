from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это мой 2 проект на Django</h1>")

def data(request):
    return HttpResponse("<h1>Страница data по заданию DJ01</h1>")

def test(request):
    return HttpResponse("<h1>Страница test по заданию DJ01</h1>")



