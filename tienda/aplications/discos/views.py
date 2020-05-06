from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Disco
from aplications.artista.models import Artista
# Create your views here.


class DiscosListView(ListView):
    template_name = "discos/lista_discos.html"
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Artista.objects.filter(
            nombre__icontains=palabra_clave,
    )

class DiscoImg(ListView):
    template_name = "disco.html"
    model = Disco
    context_object_name = 'lista'

class ListCanciones(ListView):
    template_name = "discos/canciones.html"
    model = Artista
    context_object_name = 'lista'
