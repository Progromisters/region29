# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator

class Client(models.Model):
    name = models.CharField(null=False, blank=False, max_length=32, verbose_name='Имя')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=12, null=False, blank=False, verbose_name='Телефон')
    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
