from django import forms 

class LibroFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    escritor= forms.CharField(max_length=30)
    descripcion= forms.CharField(max_length=100)    
    categoria= forms.CharField(max_length=30)    
    precio= forms.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion= forms.DateTimeField(required=False)
    imagen= forms.ImageField(required=False)

class BusquedaLibroFormulario(forms.Form):
    nombre= forms.CharField(max_length=30, required=False)

