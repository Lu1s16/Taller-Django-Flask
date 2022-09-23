from flask import Flask
from flask import render_template
from flask import request



app = Flask(__name__)



@app.route("/")
def index():
    return "hola"

@app.route("/Insertar")
def insertar():

    return render_template("metodo post.html")

@app.route("/ver", methods=["POST"]) #methods=["POST"]
def ver():

    return render_template("ver_mascotas.html")

@app.route("/vermascota/<id>", methods=["GET"])
def vermascota(id=0):



    return "Hola"


if __name__ == "__main__":
    app.run(debug=True)