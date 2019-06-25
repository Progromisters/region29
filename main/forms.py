# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from .models import Client


class ClientForm(forms.ModelForm):
    name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={
        'id': 'name',
        'class': 'app__input',
        'name': 'name',
        'placeholder': 'Ваше имя'
    }))
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Неправильный формат')
    phone = forms.CharField(validators=[phone_regex], max_length=12, required=True, widget=forms.TextInput(attrs={
        'id': 'phone',
        'class': 'app__input',
        'name': 'phone',
        'placeholder': 'Ваш телефон'
    }))
    
    class Meta:
         model = Client
         exclude = [""]