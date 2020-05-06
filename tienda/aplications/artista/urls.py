from django.contrib import admin
from django.urls import path

from . import views

app_name = "artista_app"

urlpatterns = [
    path(
        'lista-artistas/',
        views.ArtistasView.as_view(),
        name='lista-artistas'
    ),
    path(
        '',
        views.TemplateView.as_view(),
        name='inicio'
    ),
    path(
        'tienda/',
        views.CompraView.as_view(),
        name='tienda'
    ),
    path(
        'detalle-compra/<pk>/',
        views.DetalleCompra.as_view(),
        name='detalle'
    ),
    path(
        'compra-exitosa/',
        views.CompraExitosa.as_view(),
        name='exito'
    ),
]
