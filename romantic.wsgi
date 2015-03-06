#!/usr/bin/python
# coding=utf-8

import os,sys

import os, sys sys.path.append('/home/tkrodua/domains/tkr.od.ua/django') sys.path.append('/home/tkrodua') 
import django.core.handlers.wsgi application = django.core.handlers.wsgi.WSGIHandler()
# this line solved it sys.executable = '/usr/local/python-2.7.2/bin/python' os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

import django.core.handlers.wsgi application = django.core.handlers.wsgi.WSGIHandler()

apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)


sys.path.insert(0,'/home/tkrodua/domains/tkr.od.ua/django/romantiс/')
sys.path.insert(0,'/home/tkrodua/domains/tkr.od.ua/django/romantiс/romantiс/')
sys.path.insert(0,'/home/tkrodua/virtualenv/romantiс/')
sys.path.insert(0,'/home/tkrodua/domains/tkr.od.ua/django')
sys.path.insert(0,'/home/tkrodua/virtualenv/romantiс/lib/python2.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'romantiс.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
