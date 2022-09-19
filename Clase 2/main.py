from flask import Flask
from flask import render_template
from mascotas import Mascotas


app = Flask(__name__)


def Suma():

    respuesta = 2 + 2

    return respuesta

@app.route("/")
@app.route("/<name>")
@app.route("/<name>/<apellido>")
def index(name= "Jorge", apellido="Perez"):

    lista = ["Canada", "USA", "Guatemala", "Mexico"]

    return render_template("index.html", nombre=name, apellido=apellido, funcion=Suma(), mi_lista=lista)


#Aqui se estan agregando los archivos estaticos
@app.route("/numeros")
@app.route("/numeros/<int:num>")
def numeros(num=0):

    var = range(num+1)
    lista = []

    for c in var:
        lista.append(c)


    return render_template("numeros.html", lista=lista, edad=num)

  


if __name__ == "__main__":
    app.run(debug=True, port=8000)