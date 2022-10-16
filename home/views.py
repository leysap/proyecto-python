from home.models import Libro
from datetime import datetime
from django.shortcuts import render, redirect
from home.forms import LibroFormulario, BusquedaLibroFormulario

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


def ver_libros(request):
            
    nombre = request.GET.get('nombre',None)
    
    if nombre : 
        libros = Libro.objects.filter(nombre__icontains = nombre)
    else: 
        libros = Libro.objects.all()
    
    formulario = BusquedaLibroFormulario()
    return render(request,"home/ver_libros.html", {'libros': libros, 'formulario': formulario})


def acerca_de_nosotros(request):
    
    return render(request, "home/acerca_de_nosotros.html", {})

def index(request):
    return render(request, "home/index.html")