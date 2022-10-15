# from django.http import HttpResponse
# from django.template import Context, Template, loader
from home.models import Libro
from datetime import datetime
from django.shortcuts import render, redirect
from home.forms import LibroFormulario

def cargar_libro(request):
    
    if request.method == 'POST':
        
        formulario = LibroFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            descripcion = data['descripcion']
            categoria= data['categoria']
            precio= data['precio']
            fecha_creacion= data['fecha_creacion']

            if not fecha_creacion:
                fecha_creacion=datetime.now()
                
            libro = Libro(nombre=nombre, descripcion=descripcion, categoria=categoria, precio=precio,fecha_creacion=fecha_creacion)
            libro.save()
            
            return redirect("ver_libros")
        
    formulario= LibroFormulario()
    return render(request, "home/cargar_libro.html", {'formulario': formulario})

#Completar con la busqueda
def ver_libros(request):
    
    return render(request,"home/ver_libros.html", {})


def acerca_de_nosotros(request):
    
    return render(request, "home/acerca_de_nosotros.html", {})

def index(request):
    return render(request, "home/index.html")