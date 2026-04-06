#Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que
#pasa la línea en un espacio de dos dimensiones.

#La clase dispondrá de los siguientes métodos:
#● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase
#Punto, que son utilizados para inicializar los atributos.
#● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
#● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
#● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
#● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.

from ejercicio_2 import Punto

class Linea:
    def __init__(self,_punto_a,_punto_b): #Entendi aca que lo que le voy a pasar son dos instancias de Punto luego declaradas
        self._punto_a = _punto_a
        self._punto_b = _punto_b
    
    def mueve_derecha(self,distancia):
        self._punto_a.x += distancia 
        self._punto_b.x += distancia
    
    def mueve_izquierda(self,distancia):
        self._punto_a.x -= distancia 
        self._punto_b.x -= distancia

    def mueve_arriba(self,distancia):
        self._punto_a.y += distancia
        self._punto_b.y += distancia

    def mueve_abajo(self,distancia):
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia

    def ubicacion_actual(self):
        return f"Coordenadas actuales línea: ({self._punto_a.x},{self._punto_a.y});({self._punto_b.x},{self._punto_b.y})"

#el self._punto_a.y por ejemplo .y lo uso para desempaquetar el atributo y del punto a y asi con todos los metodos
#agregue el metodo ubicacion_actual para ir viendo si funcionaban las pruebas


#Instancias de Punto que voy a pasarle al objeto Linea para hacer la instancia de linea
punto_a = Punto(2,5)
punto_b = Punto(4,10)
#Instancia de linea
linea = Linea(punto_a,punto_b)
print(linea.ubicacion_actual())
#Mover linea a la derecha y arriba
linea.mueve_derecha(5)
linea.mueve_arriba(3)
print(linea.ubicacion_actual())
#Mover linea a la izquierda y abajo
linea.mueve_izquierda(20)
linea.mueve_abajo(50)
print(linea.ubicacion_actual())    