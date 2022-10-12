import pymysql

#Crear la conexion con la base de datos
def obtener_conexion():

    #Colocar la configuracion de su servidor y base de datos
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tienda"
    )


#print(obtener_conexion().get_host_info())
#print(obtener_conexion().get_server_info())
#print(obtener_conexion().get_autocommit())

