"""
WSGI config for helloworld project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os #, sys

#sys.path.append('/helloworld/helloworld')

from django.core.wsgi import get_wsgi_application

#from django.conf import settings
from django.conf import settings

import sys
sys.path.append("/home/faithmazz/projectTest/helloworld")

#path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helloworld.settings")

application = get_wsgi_application()
