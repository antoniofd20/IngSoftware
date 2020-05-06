from django.shortcuts import render
from django.views.generic import CreateView
from .models import Venta
from django.urls import reverse_lazy

# Create your views here.

class VentaCreateView(CreateView):
    template_name = "venta/formulario.html"
    model = Venta
    fields = ('__all__')
    success_url = reverse_lazy('artista_app:exito')

    def form_valid(self, form):
        return super(VentaCreateView, self).form_valid(form)
