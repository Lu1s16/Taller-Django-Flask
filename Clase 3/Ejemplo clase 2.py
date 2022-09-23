from flask import Flask
from flask import render_template

from mascotas import Mascotas

import random

#<script type="text/javascript" src="{{ url_for('static', filename='js/app.js') }}"></script>

app = Flask(__name__)


lista_mascotas = []
lista_id = []


@app.route("/")
def index():
    return "hola"

@app.route("/Insertar")
@app.route("/Insertar/<nombre>")
@app.route("/Insertar/<nombre>/<tipo>")
def insertar(nombre = None, tipo = None):

    id = random.randint(100, 1000)


    while True:

        if id in lista_id:
            id = random.randint(100, 1000)
        
        else:
            lista_id.append(id)
            break

    mensaje = ""

    if nombre == None or tipo == None:
        mensaje = "Error, no ha ingresado ningun nombre de animal"

    else:
        nueva_mascota = Mascotas(id, nombre, tipo)
        lista_mascotas.append(nueva_mascota)
        mensaje = "Se añadio una nueva mascota"

    return render_template("animales.html", msg=mensaje)


@app.route("/ver")
@app.route("/ver/<user>/<password>")
def ver(user = None, password = None):

    bandera = False

    if user == "Admin" and password == "123":
        bandera = True


    return render_template("ver_mascotas.html", lista=lista_mascotas, bandera=bandera)




if __name__ == "__main__":
    app.run(debug=True)