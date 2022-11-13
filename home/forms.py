from django import forms 

class BusquedaLibroFormulario(forms.Form):
    nombre= forms.CharField(max_length=30, required=False)

