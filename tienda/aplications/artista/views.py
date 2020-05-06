from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Artista

# Create your views here.
"""Vista de los artistas"""
class ArtistasView(ListView):
    template_name = 'artista/lista_artistas.html'
    context_object_name = 'lista'
    paginate_by = 8

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Artista.objects.filter(
            nombre__icontains=palabra_clave,
    )

"""Vista para las compras"""
class CompraView(ListView):
    template_name = 'artista/lista_compra.html'
    context_object_name = 'lista'
    paginate_by = 8

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Artista.objects.filter(
            nombre__icontains=palabra_clave,
    )

"""Detalle de la compra"""
class DetalleCompra(DetailView):
    template_name = "artista/detalle.html"
    model = Artista
    context_object_name = 'lista'

"""Compra"""
class CompraExitosa(TemplateView):
    template_name = "artista/exito.html"

class TemplateView(TemplateView):
    template_name='inicio.html'
