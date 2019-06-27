# -*- coding: utf-8 -*-
from .models import Price
from .forms import ClientForm


def prices(request):
    priceB = Price.objects.get(category='B')
    priceA = Price.objects.get(category='A')
    priceAB = Price.objects.get(category='A+B')
    priceSale = Price.objects.get(category='Скидка')
    form = ClientForm(request.POST or None)
    return locals()