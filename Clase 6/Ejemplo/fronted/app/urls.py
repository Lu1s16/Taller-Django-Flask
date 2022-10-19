from django.urls import path
from . import views

#Se crea el url de la vista de views.py
#Este archivo se va incluir en urls.py del fronted

urlpatterns = [

    #name reconoce el nombre del template
    
    path("login/", views.inicio_sesion, name="index"), #verifica el user y password
    path("home/", views.home, name="menu"), #muestra la pagina principal
    path("add/", views.add, name="agregar"),  #muestra la pagina agregar
    path("delete/<pelicula>", views.eliminar, name="menu"),
    path("vista/<pelicula>", views.vista, name="vista")

]
