# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Client


class ClientForm(forms.ModelForm):
    name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={
        'id': 'name',
        'class': 'app__input',
        'name': 'name',
        'placeholder': 'Ваше имя'
    }), error_messages={
        'required': _('Введите имя')
    })
    phone = forms.CharField(max_length=12, required=True, widget=forms.TextInput(attrs={
        'id': 'phone',
        'class': 'app__input',
        'name': 'phone',
        'placeholder': 'Ваш телефон'
    }), error_messages={
        'required': _('Введите телефон'),
        'invalid': _('Неверный формат номера')
    })
    
    class Meta:
         model = Client
         exclude = [""]