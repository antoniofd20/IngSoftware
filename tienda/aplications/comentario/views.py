from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from .models import Comentario
from django.urls import reverse_lazy

# Create your views here.

class ComentarioListView(ListView):
    model = Comentario
    template_name = "comentario/lista.html"
    context_object_name = 'lista'


class ComentarioCreateView(CreateView):
    model = Comentario
    template_name = "comentario/crear.html"
    fields = ('__all__')
    success_url = reverse_lazy('comentario_app:lista-comentarios')
 
class ComentarioView(TemplateView):
    template_name = "comentario/gracias.html"
    

