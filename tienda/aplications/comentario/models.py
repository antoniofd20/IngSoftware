from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Comentario(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    email = models.EmailField('Email', max_length=80)
    edad = models.IntegerField()
    pais = models.CharField('País', max_length=20)
    comentario = models.TextField()

    def __str__(self):
        return 'Comentario de: ' + self.nombre