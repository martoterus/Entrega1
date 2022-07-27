from django.db import models
idB=0

# Create your models here.
class bicicletas(models.Model):
    id=models.BigAutoField(primary_key=True)    
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    rodado = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    fecha_fabricacion = models.DateField()
    precio = models.IntegerField()


class repuestos(models.Model):
    tipo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    fabricante = models.CharField(max_length=30)
    fecha_fabricacion = models.DateField()
    precio = models.IntegerField()
    

class indumentaria(models.Model):
    tipo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    precio = models.IntegerField()