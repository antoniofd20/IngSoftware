from django.contrib import admin
from django.urls import path

from . import views

app_name = "disco_app"

urlpatterns = [
    path(
        'lista-discos/<pk>/',
        views.DiscosListView.as_view(),
        name='lista-discos'
    ),
    path(
        'portada/',
        views.DiscoImg.as_view(),
        name='portada'
    ),
    path(
        'prueba2/',
        views.ListCanciones.as_view(),
        name='portada'
    )
]
