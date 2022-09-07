from flask import Flask
from flask import request

app = Flask(__name__)

#Mostrando un mensaje en la pagina
@app.route("/")
def index():

    return "Hello world"

#Mostrar datos personales 
@app.route("/datos")
def datos_personales():
    nombre = request.args.get("nombre", "No se envio un parametro")
    apellido = request.args.get("apellido", "No se envio un apellido")
    edad = request.args.get("edad", "No se envio una edad")

    html = """<html>
    <head>
        <title>Pagina</title>
    </head>
    <body>
        <p>Mi nombre es: """ + "{}".format(nombre) + """</p>
        <p>Mi apellido es: """ + "{}".format(apellido) + """ </p>
        <p>Mi edad es: """ + "{}".format(edad) + """ </p>

    </body>
    </html>
    """
    
    return html

#Mostrar edad ingresando el año como parametro
@app.route("/datos2")
def datos_personales_con_año():
    nombre = request.args.get("nombre", "No se envio un parametro")
    apellido = request.args.get("apellido", "No se envio un apellido")
    año = request.args.get("año", "No se envio una edad")

    edad = 2022-int(año)

    html = """<html>
    <head>
        <title>Pagina</title>
    </head>
    <body>
        <p>Mi nombre es: """ + "{}".format(nombre) + """</p>
        <p>Mi apellido es: """ + "{}".format(apellido) + """ </p>
        <p>Mi edad es: """ + str("{}".format(edad)) + """ </p>

    </body>
    </html>
    """

    return html

#Mostrar tabla de multiplicar ingresando el numero como parametro
@app.route("/tabla")
@app.route("/tabla/<int:num>")
def tabla_multiplicar(num = 0):

    html = """<html>
    <head>
        <title>Pagina</title>
    </head>
    <body>"""

    var = 1
    texto = ""
    while(var<=10):

        operacion = num*var

        texto += "<p>" + str(num) + "*" + str(var) + "=" + str(operacion) + "</p><br>"

        var+=1

    html+=texto
    html+="""</body>
    </html>"""

    return html

#Mostrar una operación en la pagina con parametros
@app.route("/calculadora")
@app.route("/calculadora/<int:num1>/<int:num2>/<op>")
def calculadora(num1 = 0, num2 = 0, op = "suma"):

    texto = ""

    if(op == "suma"):
        operacion = num1 + num2
        texto = "El resultado de " + "{}".format(op) + " es: " + str(operacion) 
        

    elif(op == "resta"):
        operacion = num1 - num2
        texto = "El resultado de " + "{}".format(op) + " es: " + str(operacion)

    elif(op == "multi"):
        operacion = num1 * num2
        texto = "El resultado de " + "{}".format(op) + " es: " + str(operacion)
        

    elif(op == "division"):
        operacion = num1 / num2
        texto = "El resultado de " + "{}".format(op) + " es: " + str(operacion)
        

    return texto



if __name__ == "__main__":

    app.run(debug=True, port=8000)