import os
import sys

sys.path.append('/home/eclipsealtair/region29/')
sys.path.append('/home/eclipsealtair/region29/region29env/lib/python3.6/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'region29.settings'
import django
django.setup()

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()