# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from .models import Slider, Review
from .forms import ClientForm
from django.core.mail import send_mail


def home(request):
    sliders = Slider.objects.all()
    return render(request, 'main/index.html', locals())

def price(request):
    return render(request, 'main/price.html')

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'main/reviews.html', locals())

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def feedback(request):
    if request.POST:
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            
            name = request.POST['name']
            phone = request.POST['phone']
            subject = 'Новый клиент!'
            message = 'Имя: '+name+' | Номер телефона: '+phone
            sender = 'digitalrushmailer@gmail.com'
            recipient = 'avtoshkola_region29@mail.ru'
            send_mail(subject, message, sender, [recipient], fail_silently=False)

            return JsonResponse({'result': 'ok'})
        else:
            response = {}
            for i in form.errors:
                response[i] = form.errors[i][0]
            return JsonResponse({'response':response, 'result': 'error'})