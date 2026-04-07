#● Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
#cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
#(ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes
#servicios: getters y setters, método para leer la información y método para mostrar la
#información.
class Persona:
    def __init__(self,nombre_completo):
        self.nombre_completo = nombre_completo

class Libro():
    def __init__(self,autor,titulo,isbn,paginas,edicion,editorial,lugar,fecha_de_edicion):
        self.autor = autor
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_de_edicion = fecha_de_edicion
    
    def set_autor(self,nombre_completo):
        self.autor = Persona(nombre_completo)
    
    def set_titulo(self, titulo):
        self.titulo = titulo
    
    def set_isbn(self,isbn):
        self.isbn = isbn
    
    def set_paginas(self,paginas):
        self.paginas = paginas
    
    def set_edicion(self,edicion):
        self.edicion = edicion

    def set_editorial(self,editorial):
        self.editorial = editorial
    
    def set_lugar(self,lugar):
        self.lugar = lugar

    def set_fecha_de_edicion(self,fecha_de_edicion):
        self.fecha_de_edicion = fecha_de_edicion
    
    def get_autor(self):
        return self.autor.nombre_completo
    
    def get_titulo(self):
        return self.titulo

    def get_isbn(self):
        return self.isbn
    
    def get_paginas(self):
        return self.paginas
    
    def get_edicion(self):
        return self.edicion
    
    def get_editorial(self):
        return self.editorial
    
    def get_lugar(self):
        return self.lugar
    
    def get_fecha_de_edicion(self):
        return self.fecha_de_edicion
    
    #Por leer entendi ingresar datos 

    def leer_informacion(self):
        autor = input("Ingresa el nombre del autor: ")
        self.set_autor(autor)
        titulo = input("Ingrese el titulo: ")
        self.set_titulo(titulo)
        isbn = input("Ingresa el ISBN: ")
        self.set_isbn(isbn)
        paginas = int(input("Ingrese el número de páginas: "))
        self.set_paginas(paginas)
        edicion = input("Ingrese la edición: ")
        self.set_edicion(edicion)
        editorial = input("Ingrese la editorial: ")
        self.set_editorial(editorial)
        lugar = input("Ingrese el lugar (ciudad y pais): ")
        self.set_lugar(lugar)
        fecha_de_edicion = input("Ingrese la fecha de edicion: ")
        self.set_fecha_de_edicion(fecha_de_edicion)
    
    def mostrar_informacion(self):
        print(f"""
        --- Información del libro ---
        Autor:     {self.get_autor()}
        Titulo:    {self.get_titulo()}
        ISBN:      {self.get_isbn()}
        Páginas:   {self.get_paginas()}
        Edición:   {self.get_edicion()}
        Editorial: {self.get_editorial()}
        Lugar:     {self.get_lugar()}
        Fecha:     {self.get_fecha_de_edicion()}
        -----------------------
        """.strip())
    
    #PRUEBA

libro_prueba = Libro("","",0,0,"","","","") #Creo una instancia de libro con parametros vacios para poder editarlo luego con el metodo leer_informacion()
libro_prueba.leer_informacion()
libro_prueba.mostrar_informacion()
    
