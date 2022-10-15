from django.http import HttpResponse
from django.template import Context, Template, loader
from home.models import Libro, Persona
from datetime import datetime
import random
from django.shortcuts import render

def cargar_libro(request):
    
    return render(request, "home/cargar_libro.html", {})

def ver_libros(request):
    
    return render(request,"home/ver_libros.html", {})

def acerca_de_nosotros(request):
    
    return render(request, "home/acerca_de_nosotros.html", {})

def index(request):
    return render(request, "home/index.html")