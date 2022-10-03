from django.http import HttpResponse
from django.template import Context, Template, loader
from home.models import Persona
from datetime import datetime
import random


def crear_persona(request,nombre,apellido):
    persona= Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_creacion=datetime.now())
    persona.save()

    
    template= loader.get_template("crear_persona.html")
    template_renderizado= template.render({"personas": persona})
    return HttpResponse(template_renderizado)

def ver_personas(request):
    personas= Persona.objects.all()
    template=loader.get_template("ver_personas.html")
    template_renderizado= template.render({"personas": personas})
    return HttpResponse(template_renderizado)