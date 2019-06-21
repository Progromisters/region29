# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Client
from .forms import ClientForm


def home(request):
    form = ClientForm(request.POST or None)
    return render(request, 'main/index.html', locals())

def feedback(request):
    if request.POST:
        form = ClientForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, 'main/index.html', locals())