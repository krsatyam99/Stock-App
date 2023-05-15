# from django.contrib import admin
from django.urls import path
from stock import views

urlpatterns = [
    path('',views.stockspicker,name='stockspicker'),
    path('stocktracker/',views.stockstracker,name='stockstracker'),

]
