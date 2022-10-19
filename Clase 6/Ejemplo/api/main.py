
from flask import Flask
from flask import jsonify


from Lista import lista_peliculas

app = Flask(__name__)

lista = lista_peliculas()


@app.route("/")
def index():

    return "Hello world"

#al usar post en django con requests.post
#~se debe especificar que es post aqui
@app.route("/login/<user>/<password>", methods=["POST"])
def login(user, password):

    print(user)
    print(password)

    if user == "Admin" and password == "123":


        return jsonify({"Mensaje": "Usuario correcto"})

    else:


        return jsonify({"Mensaje": "Usuario incorrecto"})

@app.route("/agregar/<pelicula>/<genero>/<descripcion>", methods=["post"])
def agregar(pelicula, genero, descripcion):

    

    mensaje = lista.insertar(pelicula, genero, descripcion)

    return jsonify(mensaje)


@app.route("/ver")
def ver():

    mensaje = lista.mostrar()

    return jsonify(mensaje)


@app.route("/ver_individual/<pelicula>", methods=["GET"])
def ver_individual(pelicula):

    mensaje = lista.mostrar_individual(pelicula)

    return jsonify(mensaje)


@app.route("/eliminar/<pelicula>", methods=["delete"])
def eliminar(pelicula):

    mensaje = lista.eliminar(pelicula)

    return jsonify(mensaje)





if __name__ == "__main__":

    app.run(debug=True, port=4000)