# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Client, Slider, Review

class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.fields]
    
    class Meta:
        model = Client
admin.site.register(Client, ClientAdmin)

class SliderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Slider._meta.fields]

    class Meta:
        model = Slider
admin.site.register(Slider, SliderAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Review._meta.fields]

    class Meta:
        model = Review
admin.site.register(Review, ReviewAdmin)