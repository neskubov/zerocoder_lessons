from django.db import models

# Create your models here.

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    user_name = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} ({self.user_id})'