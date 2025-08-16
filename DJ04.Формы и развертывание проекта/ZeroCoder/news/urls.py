from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('create_news', views.create_news, name='add_news')
]