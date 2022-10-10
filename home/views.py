from django.http import HttpResponse
from django.template import Context, Template, loader
from home.models import Persona
from datetime import datetime
import random
from django.shortcuts import render


def crear_persona(request,nombre,apellido):
    persona= Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_creacion=datetime.now())
    persona.save()

    # template= loader.get_template("crear_persona.html")
    # template_renderizado= template.render({"personas": persona})
    return render(request, "home/crear_persona.html", {"personas": persona})

def ver_personas(request):
    personas= Persona.objects.all()
    # template=loader.get_template("ver_personas.html")
    # template_renderizado= template.render({"personas": personas})
    
    return render(request, "home/ver_personas.html", {"personas": personas})

def index(request):
    return render(request, "home/index.html")