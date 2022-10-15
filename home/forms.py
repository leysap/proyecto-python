from django import forms 

class LibroFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    descripcion= forms.CharField(max_length=50)    
    categoria= forms.IntegerField()
    precio= forms.DecimalField(max_digits=5, decimal_places=2)
    fecha_creacion= forms.DateTimeField(required=False)
    
