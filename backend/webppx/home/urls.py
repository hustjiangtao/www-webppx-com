# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
