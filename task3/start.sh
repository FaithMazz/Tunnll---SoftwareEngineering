#!/bin/bash


# Start Gunicorn processes
echo Starting Gunicorn.
cd helloworld
exec gunicorn helloworld.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3


#exec gunicorn helloworld.wsgi
#exec gunicorn wsgi.py
#
#

#for docker, use exec gunicorn helloworld.wsgi:application \
#for local, use exec gunicorn wsgi:application \
