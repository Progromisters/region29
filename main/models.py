# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False, verbose_name='Имя')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Неверный формат номера')
    phone = models.CharField(validators=[phone_regex], max_length=12, null=False, blank=False, verbose_name='Телефон')
    
    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'

class Slider(models.Model):
    title = models.CharField(max_length=32, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    
    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'
        ordering = ('id',)

def image_name(instance, filename):
    filename = instance.surname + '.' + filename.split('.')[1]
    return 'reviews/{}'.format(filename)
        
class Review(models.Model):
    img = models.ImageField(upload_to=image_name, verbose_name='Фото')
    name = models.CharField(max_length=16, null=False, blank=False, verbose_name='Имя')
    surname = models.CharField(max_length=16, verbose_name='Фамилия')
    link = models.CharField(max_length=64, verbose_name='Ссылка')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('id',)