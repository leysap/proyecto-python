from home.models import Libro
from django.shortcuts import render
from home.forms import  BusquedaLibroFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import  DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

@login_required
def ver_libros(request):
            
    nombre = request.GET.get('nombre',None)
    
    if nombre : 
        libros = Libro.objects.filter(nombre__icontains = nombre)
    else: 
        libros = Libro.objects.all()
    
    formulario = BusquedaLibroFormulario()
    return render(request,"home/ver_libros.html", {'libros': libros, 'formulario': formulario})

@login_required
def acerca_de_nosotros(request):
    
    return render(request, "home/acerca_de_nosotros.html", {})

@login_required
def index(request):
    return render(request, "home/index.html")

class CargarLibro(LoginRequiredMixin,CreateView):
    model= Libro
    success_url= '/ver-libros/'
    template_name= 'home/cargar_libro.html'
    fields= ['nombre', 'escritor', 'descripcion', 'categoria','precio', 'fecha_creacion', 'imagen']
    
class EditarLibro(LoginRequiredMixin, UpdateView):
    model=Libro
    success_url= '/ver-libros/'
    template_name= 'home/editar_libro.html'
    fields= ['nombre', 'escritor', 'descripcion','categoria', 'precio', 'fecha_creacion', 'imagen']
    
    
class EliminarLibro(LoginRequiredMixin, DeleteView):
    model=Libro
    success_url='/ver-libros/'
    template_name='home/eliminar_libro.html'

class VerLibro(DetailView):
    model= Libro 
    template_name='home/ver_libro.html'