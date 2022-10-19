from Peliculas import peliculas

class lista_peliculas:

    def __init__(self):

        self.lista = []


    def insertar(self, pelicula, genero, descripcion):

        nueva_pelicula = peliculas(pelicula, genero, descripcion)

        self.lista.append(nueva_pelicula)

        msg = {"Mensaje:": "Se agrego la pelicula correctamente"}

        return msg


    def eliminar(self, pelicula):

        cont = 0

        for c in self.lista:

            if c.pelicula == pelicula:

                self.lista.pop(cont)

                msg = {"Mensaje": "Se elimino la pelicula correctamente"}

                return msg

            cont+=1

        
        msg = {"Mensaje:": "Esta pelicula no existe"}

        return msg
        

        

    def mostrar(self):

        lista = []

        for c in self.lista:
            pelicula = {
                "Pelicula": c.pelicula,
                "Genero": c.genero,
                "Descripcion": c.descripcion
            }

            lista.append(pelicula)


        return lista

    
    def mostrar_individual(self, pelicula):


        cont = 0

        for c in self.lista:

            if c.pelicula == pelicula:

                pelicula = {
                    "Pelicula": c.pelicula,
                    "Genero": c.genero,
                    "Descripcion": c.descripcion
                }

                return pelicula

            cont+=1

        error = { "Mensaje:": "No existe esta pelicula"}

        return error




