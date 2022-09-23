from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from mascotas import Mascotas



app = Flask(__name__)


lista_mascotas = []
lista_id = []


@app.route("/")
def index():
    return "nueva pagina"

@app.route("/ver", methods=["GET"])
def ver():

    mascotas = []

    for c in lista_mascotas:
        mascota = {"ID": c.id, "Nombre": c.nombre, "Animal": c.animal}
        mascotas.append(mascota)

    return jsonify({"Mascotas": mascotas, "Mensaje": "Correcto"})


@app.route("/ver/<id>")
def vermascota(id):

    if id in lista_id:
        print("si existe el id")

        for c in lista_mascotas:

            if id == c.id:
                mascota = {"id": c.id, "Nombre": c.nombre, "Animal": c.animal}
                break

        return jsonify({"Mascota": mascota})

    else:

        return jsonify({"Mensaje": "No existe"})
    
@app.route("/Insertar", methods=["POST"])
def registrar():

    #print(request.json)

    if request.json["id"] in lista_id:
        return jsonify({"Mensaje": "Error, el id ya existe"})

    else:
        lista_id.append(request.json["id"])
        nueva_mascota = Mascotas(request.json["id"], request.json["nombre"], request.json["animal"])
        lista_mascotas.append(nueva_mascota)
        return jsonify({"Mensaje:": "Se agrego la mascota correctamente"})
    
    

@app.route("/actualizar/<id>", methods=["PUT"])
def actualizar(id):

    if id in lista_id:
        print("Si existe")
        for c in lista_mascotas:
            if c.id == id:
                c.animal = request.json["animal"]
                c.nombre = request.json["nombre"]
                break

        return jsonify({"Mensaje": "Se actualizo correctamente"})

    else:
        return jsonify({"Mensaje": "No existe el id"})


@app.route("/eliminar/<id>", methods=["DELETE"])
def eliminar(id):

    index = 0
    index_id = 0

    if id in lista_id:
        for c in lista_mascotas:
            if c.id == id:
                break
            
            index+=1

        lista_mascotas.pop(index)

        for c in lista_id:
            if c == id:
                break

            index+=1

        lista_id.pop(index_id)

        return jsonify({"Mensaje": "Se elimino correctamente"})

    else:


        return jsonify({"Mensaje": "No existe el id"})




def pagina_error(error):

    return "<h1>Esta pagina no existe</h1>", 404

if __name__ == "__main__":

    app.register_error_handler(404, pagina_error)
    app.run(debug=True)