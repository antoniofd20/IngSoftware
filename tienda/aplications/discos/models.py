from django.db import models
from aplications.artista.models import Artista

# Create your models here.
class Disco(models.Model):
    titulo = models.CharField('Titulo', max_length=40)
    artista = models.OneToOneField(Artista, on_delete=models.CASCADE, primary_key=True)
    duracion = models.TimeField()
    lista_canciones = models.TextField()
    year = models.CharField('Año publicación', max_length=4)
    portada = models.ImageField(upload_to='discos', blank=True, null=True)
    precio = models.FloatField()
    class Meta:
        ordering = ['titulo', 'artista'] #Ordenar -----importante

    def __str__(self):
        return self.titulo + ' de: ' + self.artista.nombre + ' ' + self.artista.last_name
