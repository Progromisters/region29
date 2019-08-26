# -*- coding: utf-8 -*-
from django.urls import path
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemap import StaticViewSitemap


robots = 'User-agent: *\n' \
         'Disallow: /admin\n' \
         'Sitemap: http://водитель29.рф/sitemap.xml'

sitemaps = {
    'static': StaticViewSitemap,
    }

manifest = '{"name":"Автошкола Регион29",' \
           '"short_name":"Регион29",' \
           '"start_url":"/",' \
           '"display":"standalone",' \
           '"theme_color":"#000",' \
           '"background_color":"#000",' \
           '"description":"Автошкола Северодвинска",' \
           '"icons":' \
            '[{"src":"img/favicon-16x16.png",' \
            '"sizes":"16x16",' \
            '"type":"image/png"},' \
            '{"src":"img/favicon-32x32.png",' \
            '"sizes":"32x32",' \
            '"type":"image/png"},' \
            '{"src":"img/favicon-196x196.png",' \
            '"sizes":"196x196",' \
            '"type":"image/png"},' \
            '{"src":"img/favicon-196x196.png",' \
            '"sizes":"512x512",' \
            '"type":"image/png"}]}'

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback', views.feedback, name='feedback'),
    path('цены', views.price, name='price'),
    path('отзывы', views.reviews, name='reviews'),
    path('об-автошколе', views.about, name='about'),
    path('контакты', views.contacts, name='contacts'),
    path('robots.txt', lambda r: HttpResponse(robots, content_type="text/plain; charset=utf-8")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('manifest.json', lambda r: HttpResponse(manifest, content_type="application/json"))
]
