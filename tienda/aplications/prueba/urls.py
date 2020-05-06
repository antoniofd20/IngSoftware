from django.contrib import admin
from django.urls import path
from . import views

app_name = 'prueba_app'

urlpatterns = [
    path(
        'prueba/',
        views.PruebaView.as_view(),
        name = 'prueba'
    ),
]