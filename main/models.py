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
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Price(models.Model):
    category = models.CharField(max_length=32, null=False, blank=False, verbose_name='Категория')
    price = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Цена')
    
    def __str__(self):
        return '{}'.format(self.category)

    class Meta:
        verbose_name = 'Расценка'
        verbose_name_plural = 'Расценки'
        ordering = ('id',)