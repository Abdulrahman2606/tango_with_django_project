# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:59:17 2023

@author: abdul
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
