from db import obtener_conexion


def insertar(id, animal, descripcion, precio):
    conexion = obtener_conexion()
    #Crear cursor para ejecutar las consultas
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO mascotas(id, animal, descripcion, precio) VALUES (%s, %s, %s, %s)",
        (id, animal, descripcion, precio))

    #Guardar cambios
    conexion.commit()
    conexion.close()


def obtener_animales():
    conexion = obtener_conexion()
    mascotas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, animal, descripcion, precio FROM mascotas")
        mascotas = cursor.fetchall()

    conexion.close()
    return mascotas




def eliminar_mascota(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM mascotas WHERE id = %s", (id,))
    
    conexion.commit()
    conexion.close()

def obtener_mascota_id(id):
    conexion = obtener_conexion()
    mascota = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, animal, descripcion, precio FROM mascotas WHERE id = %s", (id,))
        
        mascota = cursor.fetchone()

    conexion.close()
    return mascota


def actualizar(animal, descripcion, precio, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE mascotas SET animal = %s, descripcion= %s, precio = %s WHERE id = %s",
                        (animal, descripcion, precio, id))

    conexion.commit()
    conexion.close()

#insertar(40, "gato", "Es pequeño", 150)

#eliminar_mascota(40)



#print(obtener_mascota_id(50))

#actualizar("Pez", "Es nuevo", 50, 40)

#print(obtener_animales())

#print(obtener_id()[0])