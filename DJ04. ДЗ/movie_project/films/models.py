from django.db import models

# Create your models here.
class FilmsPost(models.Model):
    title = models.CharField('Название фильма', max_length=50)
    description = models.TextField('Описание')
    review = models.TextField('Отзыв')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
