from django.db import models

    
class Libro(models.Model): #Prueba Leo
    nombre= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=100)    
    categoria= models.CharField(max_length=30) 
    precio= models.DecimalField(max_digits=10, decimal_places=3)
    fecha_creacion= models.DateTimeField()
