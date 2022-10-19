
from django.shortcuts import render

#Para hacer los request
import requests

#Para leer los json
import json

#para redireccionar rutas
from django.shortcuts import redirect

# Create your views here.

endpoint = "http://127.0.0.1:4000/"


#Vista funcion para el inicio de sesion
def inicio_sesion(request):

    #Verifica que metodo esta realizando la pagina.
    #Cuando se ingresa a la pagina por url se realiza un metodo get
    if request.method == "GET":

        return render(request, "index.html", {})


    #Cuando se activa el boton del from, la pagina realiza un metodo post
    elif request.method == "POST":
    
        #Verifica que los campos del form vengan llenos
        if request.POST["user"] and request.POST["password"]:

            user = request.POST["user"]
            password = request.POST["password"]


            #Se hace la peticion a la APi de flask
            response = requests.post(endpoint+"login/"+user+"/"+password).text

            print(response)

            contenido = json.loads(response)

            mensaje = contenido["Mensaje"]

            if mensaje == "Usuario correcto":

                return redirect("http://127.0.0.1:8000/home/")

            elif mensaje == "Usuario incorrecto":

                return render(request, "index.html", {"msg":mensaje})

        else:

            return render(request, "index.html", {"msg": "No ha llenado los campos"})
        

   


#Vista funcion para el home que incluye la tabla de las peliculas
def home(request, msg=None):

    lista = requests.get(endpoint+"ver").text

    contenido = json.loads(lista)

    if msg != None:


        return render(request, "menu.html", {"peliculas": contenido, "msg":msg})


    if msg == None:

        return render(request, "menu.html", {"peliculas": contenido})
    



#Vista funcion para agregar las peliculas
def add(request):

    if request.method == "GET":

    
        return render(request, "agregar.html", {})

    elif request.method == "POST":

        if request.POST["pelicula"] and request.POST["genero"] and request.POST["descripcion"]:

            pelicula = request.POST["pelicula"]
            genero = request.POST["genero"]
            descripcion = request.POST["descripcion"]

            response = requests.post(endpoint+"agregar/"+pelicula+"/"+genero+"/"+descripcion).text

            print(response)

            contenido = json.loads(response)

            mensaje = contenido["Mensaje:"]



            return render(request, "agregar.html", {"msg": mensaje})

        
        else:

            return render(request, "agregar.html", {"msg": "Falta llenar los campos"})


#Vista funcion para eliminar las peliculas
def eliminar(request, pelicula):

    if request.method == "POST":

        response = requests.delete(endpoint+"eliminar/"+pelicula).text

        contenido = json.loads(response)

        mensaje = contenido["Mensaje"]

        print(mensaje)

        #Se retorna la funcion home, el cual renderiza home.html
        return home(request, mensaje)

#Vista funcion para ver una pelicula individual con su descripcion
def vista(request, pelicula):

    if request.method == "POST":

        response = requests.get(endpoint+"ver_individual/"+pelicula).text

        contenido = json.loads(response)

        print("pelicula")
        print(contenido)
        return render(request, "vista.html", {"pelicula":contenido})
