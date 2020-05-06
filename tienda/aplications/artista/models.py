from django.db import models

# Create your models here.
class Artista(models.Model):

    GENEROS = (
        ('0', 'Pop'),
        ('1', 'Rock'),
        ('2', 'Metal'),
        ('3', 'Electrónica'),
        ('4', 'Reggaeton'),
        ('5', 'Baladas'),
        ('6', 'Regional mexicano'),
        ('7', 'Banda'),
        ('8', 'Cumbia'),
        ('9', 'Salsa'),
        ('10', 'Alternativa'),
        ('11', 'Rap')
    )

    nombre = models.CharField('Nombre(s)', max_length=20)
    last_name  = models.CharField('Apellido', max_length=15, blank=True)
    year = models.CharField('Año de inicio', max_length=4)
    numero_albums = models.IntegerField()
    genero = models.CharField('Género', max_length=20, choices=GENEROS)
    descripcion = models.TextField('Descripción')

    class Meta:
        ordering = ['nombre', 'last_name']
        
    def __str__(self):
        return self.nombre + ' ' + self.last_name
