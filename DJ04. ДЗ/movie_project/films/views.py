from django.shortcuts import render, redirect
from .models import FilmsPost
from .forms import Films_postForm

def index(request):
    films = FilmsPost.objects.all()
    return render(request, 'films/index.html',{'films': films})

def add_film(request):
    error = ""
    if request.method == 'POST':
        form = Films_postForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Данные были заполнены некорректно"
    form = Films_postForm()
    return render(request, 'films/add_film.html', {'form': form, 'error': error})
