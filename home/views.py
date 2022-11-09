from home.models import Libro
from datetime import datetime
from django.shortcuts import render, redirect
from home.forms import LibroFormulario, BusquedaLibroFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

@login_required
def cargar_libro(request):
    
    if request.method == 'POST':
        
        formulario = LibroFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            escritor = data['escritor']
            descripcion = data['descripcion']
            categoria= data['categoria']
            precio= data['precio']
            fecha_creacion= data['fecha_creacion']
            creador = data['creador']
            

            if not fecha_creacion:
                fecha_creacion=datetime.now()
                
            libro = Libro(nombre=nombre, escritor=escritor, descripcion=descripcion, categoria=categoria, precio=precio, fecha_creacion=fecha_creacion, creador=creador)
            libro.save()
            
            return redirect("ver_libros")
        else:
            return render(request, 'home/cargar_libro.html', {'formulario': formulario})
        
    formulario= LibroFormulario()
    return render(request, "home/cargar_libro.html", {'formulario': formulario})

@login_required
def ver_libros(request):
            
    nombre = request.GET.get('nombre',None)
    
    if nombre : 
        libros = Libro.objects.filter(nombre__icontains = nombre)
    else: 
        libros = Libro.objects.all()
    
    formulario = BusquedaLibroFormulario()
    return render(request,"home/ver_libros.html", {'libros': libros, 'formulario': formulario})


# funcion editar 
@login_required
def editar_libro(request,id):
    libro= Libro.objects.get(id=id)
    
    if request.method=='POST':
        formulario= LibroFormulario(request.POST)
        if formulario.is_valid():
            datos= formulario.cleaned_data
            libro.nombre=datos['nombre']
            libro.escritor=datos['escritor']
            libro.descripcion=datos['descripcion']
            libro.categoria=datos['categoria']
            libro.precio=datos['precio']
            libro.fecha_creacion=datos['fecha_creacion']
            libro.creador=datos['creador']
            libro.save()
            return redirect('ver_libros')
        else:
            return render(request, 'home/cargar_libro.html', {'libro': libro,'formulario': formulario})
      
    formulario= LibroFormulario(
        initial={
            'nombre': libro.nombre,
            'escritor': libro.escritor,
            'descripcion':libro.descripcion,
            'categoria':libro.categoria,
            'precio':libro.precio,
            'fecha_creacion':libro.fecha_creacion,
            'creador':libro.creador,
            }
        )
      
    return render(request, 'home/editar_libro.html', {'libro': libro,'formulario': formulario})

#funcion eliminar
@login_required
def eliminar_libro(request,id):
    libro= Libro.objects.get(id=id)
    libro.delete()
    return redirect('ver_libros')


@login_required
def acerca_de_nosotros(request):
    
    return render(request, "home/acerca_de_nosotros.html", {})

@login_required
def index(request):
    return render(request, "home/index.html")



#VERSION CLASES BASADAS EN VISTAS: - FALTA EL BUSCADOR-
class ListaLibros(LoginRequiredMixin,ListView):
    model=Libro
    template_name='home/ver_libros.html'
    
    
class CargarLibro(LoginRequiredMixin,CreateView):
    model= Libro
    success_url= '/ver-libros/'
    template_name= 'home/cargar_libro.html'
    fields= ['nombre', 'escritor', 'descripcion', 'categoria','precio', 'fecha_creacion', 'imagen', 'creador']
    
    
class EditarLibro(LoginRequiredMixin, UpdateView):
    model=Libro
    success_url= '/ver-libros/'
    template_name= 'home/editar_libro.html'
    fields= ['nombre', 'escritor', 'descripcion','categoria', 'precio', 'fecha_creacion', 'imagen', 'creador']
    
    
class EliminarLibro(LoginRequiredMixin, DeleteView):
    model=Libro
    success_url='/ver-libros/'
    template_name='home/eliminar_libro.html'

class VerLibro(DetailView):
    model= Libro 
    template_name='home/ver_libro.html'