# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback', views.feedback, name='feedback'),
    path('цены', views.price, name='price'),
    path('отзывы', views.reviews, name='reviews'),
    path('об-автошколе', views.about, name='about'),
    path('контакты', views.contacts, name='contacts'),
    path('robots.txt', lambda r: HttpResponse("User-agent: *\nDisallow: /admin", content_type="text/plain")),
]
