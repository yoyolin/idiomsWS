__author__ = 'Lenovo'
from django.conf.urls import url,include
from django.contrib import admin
from django.core.urlresolvers import reverse
import views
from django.conf.urls import url

from . import views

app_name = 'idiomsapp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^idioms', views.idiomsPost, name='idioms'),
    url(r'^haha', views.result, name = 'result')
    # url(r'^write', views.write, name='write'),
]
