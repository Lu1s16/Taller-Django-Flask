from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import controladores

app = Flask(__name__)


#Rutas


@app.route("/")
def index():

    return render_template("home.html")





@app.route("/login", methods=["POST"])
def login():
    name = request.form["name"]
    password = request.form["password"]

    if name == "Admin" and password == "123":
        return redirect("/add")

    else:
        return redirect("/")



@app.route("/add", methods=["GET"])
def add():

    return render_template("add.html")


@app.route("/agregar", methods=["POST"])
def agregar():

    id = request.form["id"]
    animal = request.form["animal"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]

    controladores.insertar(int(id), animal, descripcion, float(precio))
    return redirect("/add")

@app.route("/vista", methods=["GET"])
def vista():

    mascotas = controladores.obtener_animales()
    return render_template("vista.html", mascotas=mascotas)

@app.route("/eliminar", methods=["POST"])
def eliminar():
    controladores.eliminar_mascota(request.form["id"])

    return redirect("/vista")




if __name__ == "__main__":
    app.run(debug=True)


