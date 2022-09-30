from django.http import HttpResponse
from django.template import Context, Template, loader
from home.models import Persona
from datetime import datetime
import random


def crear_persona(request):
    persona1= Persona(nombre="Brad", apellido="Pitt", edad=random.randrange(1,99),fecha_creacion=datetime.now())
    persona2= Persona(nombre="Jennifer", apellido="Aniston", edad=random.randrange(1,99),fecha_creacion=datetime.now())
    persona3= Persona(nombre="George", apellido="Clooney", edad=random.randrange(1,99),fecha_creacion=datetime.now())
    persona1.save()
    persona2.save()
    persona3.save()
    
    template= loader.get_template("crear_persona.html")
    template_renderizado= template.render({})
    return HttpResponse(template_renderizado)

def ver_personas(request):
    personas= Persona.objects.all()
    template=loader.get_template("ver_personas.html")
    template_renderizado= template.render({"personas": personas})
    return HttpResponse(template_renderizado)