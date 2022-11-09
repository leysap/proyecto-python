from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Libro(models.Model): 
    nombre= models.CharField(max_length=100)
    escritor= models.CharField(max_length=30)
    descripcion= RichTextField(null=True)   
    categoria= models.CharField(max_length=30) 
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion= models.DateTimeField()
    imagen= models.ImageField(upload_to="libros", null=True, blank=True)
    creador= models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}'
   