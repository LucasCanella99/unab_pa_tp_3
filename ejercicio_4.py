#Desarrolla una clase Cancion con los siguientes atributos:
#● titulo: una variable String que guarda el título de la canción.
#● autor: una variable String que guarda el autor de la canción.
#Con los siguientes métodos:
#● Cancion(String, String): constructor que recibe como parámetros el título y el autor de la
#canción (por este orden).
#● get_titulo(): devuelve el título de la canción.
#● get_autor(): devuelve el autor de la canción.
#● set_titulo(String): establece el título de la canción.
#● set_autor(String): establece el autor de la canción

class Cancion:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self,autor):
        self.autor = autor
    
#Pruebas

cancion_1 = Cancion("tema_prueba","Yo")
print(cancion_1.get_titulo())
print(cancion_1.get_autor())
cancion_1.set_titulo("tema nuevo")
cancion_1.set_autor("juancito")
print(cancion_1.get_titulo())
print(cancion_1.get_autor())
