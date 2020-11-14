from django.db import models

import datetime

# Create your models here.


class Clientes(models.Model):
    nombre=models.CharField(max_length=35)
    apellido=models.CharField (null= True, max_length=35)
    telefono=models.CharField(max_length=8)
    correo=models.EmailField()
    direccion=models.CharField(max_length=50)
    
    def __str__(self):
        return "%s %s"%(self.nombre, self.apellido)

class Estado(models.Model):
    tipo_estado = models.CharField(max_length=100) 
    def _str_(self):
        return self.tipo_estado
		

class Proveedor(models.Model):
    proveedor = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def _str_(self):
        return self.proveedor

class Puja(models.Model):
	tiempo=(datetime.date.today()+datetime.timedelta(days=0))
	cantidad = models.CharField(max_length=5)

	

class Vehiculo(models.Model):
    tipo  = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo= models.CharField(max_length=100)
    precio = models.FloatField()
    created=models.DateTimeField(null= True,auto_now_add=True)
    updated=models.DateTimeField(null= True,auto_now_add=True)
    puja = models.FloatField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    foto  = models.ImageField(blank=True, null=True, upload_to ='vehiculos')


class Fotos(models.Model):
    fotos = models.ImageField(blank=True, null=True, upload_to ='vehiculos')
    vehiculo = models.ForeignKey(Vehiculo,  on_delete=models.CASCADE)

    def _str_(self):
        return self.fotos.url

