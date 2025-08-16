from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('data', views.data, name='page3'),
    path('test', views.test, name='page4')
]