from .models import FilmsPost
from django.forms import ModelForm, TextInput, Textarea

class Films_postForm(ModelForm):
    class Meta:
        model = FilmsPost
        fields = ['title', 'description', 'review']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок фильма'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание фильма'
            }),
            'review': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание фильма'
            }),
        }