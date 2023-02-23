from django.db import models
from django.urls import reverse


class AppModel(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя')
    status = models.CharField(max_length=128, verbose_name='Хто')
    age = models.IntegerField(verbose_name='Возраст')

    def get_absolute_url(self):
        return reverse('chosed', kwargs={'friend_name': self.name})

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Друзья'
        verbose_name_plural = 'Друзья'
        ordering = ['name']
