# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback', views.feedback, name='feedback'),
    path('price', views.price, name='price'),
    path('reviews', views.reviews, name='reviews')
]
