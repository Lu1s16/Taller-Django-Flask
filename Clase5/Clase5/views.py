from django.http import HttpResponse

from django.template import Template
from django.template import Context

import datetime


def index(request):

    return HttpResponse("Hello World!")


def calcular_edad(request, año=0):


    actual = 2022

    Edad = actual-año

    mensaje = "Mi edad actual es: " + str(Edad)

    return HttpResponse(mensaje)


def plantilla(request):

    documento = open("C:/Users/Luis/Desktop/Curso Django/Clase5/Clase5/plantillas/index.html")

    plantilla = Template(documento.read())

    documento.close()

    contexto = Context()

    html = plantilla.render(contexto)

    return HttpResponse(html)


def Mostrar_datos(request, nombre, apellido):

    fecha_actual = datetime.datetime.now()

    documento = open("C:/Users/Luis/Desktop/Curso Django/Clase5/Clase5/plantillas/ejemplo.html")

    plantilla = Template(documento.read())

    documento.close()


    contexto = Context({"nombre": nombre, "apellido": apellido, "fecha":fecha_actual})

    html = plantilla.render(contexto)

    return HttpResponse(html)






