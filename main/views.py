# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from .forms import ClientForm


def home(request):
    form = ClientForm(request.POST or None)
    return render(request, 'main/index.html', locals())

def feedback(request):
    if request.POST:
        name = request.POST["name"]
        phone = request.POST["phone"]
        print(name)
        print(phone)
        # Client.objects.create(
        #     name=name,
        #     phone=phone
        # )
    return HttpResponse('')