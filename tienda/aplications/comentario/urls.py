from django.contrib import admin
from django.urls import path

from . import views

app_name = "comentario_app"

urlpatterns = [
    path(
        'lista-comentarios/',
        views.ComentarioListView.as_view(),
        name='lista-comentarios'
    ),
    path(
        'crear-comentario/',
        views.ComentarioCreateView.as_view(),
        name='crear-comentario'
    ),
    path(
        'gracias/',
        views.ComentarioView.as_view(),
        name='gracias'
    ),
]
