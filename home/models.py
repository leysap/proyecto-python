from django.db import models

class Persona(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    fecha_creacion= models.DateTimeField(null=True)
    
class Libros(models.Model): #Prueba Leo
    nombre= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=50)
    categoria= models.IntegerField(max_length=50)
    precio= models.DecimalField(max_digits=5, decimal_places=2)
    fecha_creacion= models.DateTimeField()
