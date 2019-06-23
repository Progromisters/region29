# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from .models import Price
from .forms import ClientForm


def home(request):
    priceB = Price.objects.get(category='B')
    priceA = Price.objects.get(category='A')
    priceAB = Price.objects.get(category='A+B')
    priceSale = Price.objects.get(category='Скидка')
    form = ClientForm(request.POST or None)
    return render(request, 'main/index.html', locals())

def feedback(request):
    if request.POST:
        form = ClientForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return JsonResponse({'result': 'ok'})
        else:
            response = {}
            for i in form.errors:
                response[i] = form.errors[i][0]
            return JsonResponse({'response':response, 'result': 'error'})