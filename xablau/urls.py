from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('hello/','xablau.views.hello'),
    url('login/?','xablau.views.login')
]
