from django.db import models

# Create your models here.
class Venta(models.Model):
    TIPO = (
        ('0','Débito'),
        ('1','Crédito'),
    )

    """Datos de la tarjeta"""
    banco = models.CharField('Banco', max_length=20)
    tipo = models.CharField('Tipo', max_length=10,  blank=True)
    numero = models.IntegerField('Numero de la tarjeta')
    nombre = models.CharField('Nombre del propietario', max_length=40)
    fecha = models.DateField('Caducidad', auto_now=False, auto_now_add=False)
    digitos = models.IntegerField('Clave 3 digitos')

    """Datos del cliente"""
    nombre_cliente = models.CharField('Nombre', max_length=20, blank=True)
    apellido_paterno = models.CharField('Apellido paterno', max_length=15)
    apellido_materno = models.CharField('Apellido materno', max_length=15)
    email = models.EmailField('Email', max_length=40)
    calle_numero = models.CharField('Calle y numero', max_length=40)
    colonia = models.CharField('Colonia', max_length=20)
    delegacion = models.CharField('Delegación', max_length=15)
    estado = models.CharField('Estado', max_length=15)
    pais = models.CharField('País', max_length=15)
    codigo_postal = models.CharField('Calle y numero', max_length=5)

    def __str__(self):
        return self.banco + ' ' + self.tipo
