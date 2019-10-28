# -*- coding: utf-8 -*-
from django import forms
# from django.core.validators import RegexValidator
from .models import Client


class ClientForm(forms.ModelForm):
    name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={
        'id': 'name',
        'class': 'app__input',
        'name': 'name',
        'placeholder': 'Ваше имя'
    }))
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Неправильный формат')
    phone = forms.CharField(max_length=16, required=True, widget=forms.TextInput(attrs={
        'id': 'phone',
        'class': 'app__input',
        'name': 'phone',
        'placeholder': '+7(___)___-__-__'
    }))
    
    class Meta:
         model = Client
         exclude = [""]