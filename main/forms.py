# -*- coding: utf-8 -*-
from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={
        'id': 'name',
        'name': 'name',
        'placeholder': 'Ваше имя'
    }), error_messages={
        'required': 'Введите имя'
    })
    phone = forms.CharField(max_length=12, required=True, widget=forms.TextInput(attrs={
        'id': 'phone',
        'name': 'phone',
        'placeholder': 'Ваш телефон'
    }), error_messages={
        'required': 'Введите телефон',
        'invalid': 'Неверный формат номера'
    })
    
    class Meta:
         model = Client
         exclude = [""]