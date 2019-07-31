# -*- coding: utf-8 -*-
from django.urls import path
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemap import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap,
    }

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback', views.feedback, name='feedback'),
    path('цены', views.price, name='price'),
    path('отзывы', views.reviews, name='reviews'),
    path('об-автошколе', views.about, name='about'),
    path('контакты', views.contacts, name='contacts'),
    path('robots.txt', lambda r: HttpResponse("User-agent: *\nDisallow: /admin\nSitemap: http://водитель29.рф/sitemap.xml", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('manifest.json', lambda r: HttpResponse('{"name": "Автошкола Регион29","short_name": "Регион29","start_url": "/",'
                                                 '"display": "standalone","theme_color": "#000", "background_color": "#fff"}', content_type="application/json"))
]
