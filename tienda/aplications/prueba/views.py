from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PruebaView(TemplateView):
    template_name = "prueba/prueba1.html"

class InicioView(TemplateView):
    template_name = "prueba/inicio.html"
