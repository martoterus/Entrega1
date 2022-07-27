from django.db import models

# Create your models here.
class bicicletas(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    rodado = models.IntegerField(max_length=30)
    color = models.CharField(max_length=30)
    fecha_fabricacion = models.DateField()
    precio = models.IntegerField(max_length=30)


class repuestos(models.Model):
    tipo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    fabricante = models.CharField(max_length=30)
    fecha_fabricacion = models.DateField()
    precio = models.IntegerField(max_length=30)
    

class indumentaria(models.Model):
    tipo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    precio = models.IntegerField(max_length=30)