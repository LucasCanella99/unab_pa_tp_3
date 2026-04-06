#● Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente
#constructor que recibe ambos valores.
#● Definir métodos tales como:
#○ eje_x
#○ eje_y
#○ impresion (método que devuelve en representación de string ambos valores)
#○ opuesto (método que devuelve el punto opuesto -es decir con los atributos
#negativos-)
#○ Cualquier otro método que considere importante

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def eje_x(self):
        return self.x
    
    def eje_y(self):
        return self.y
    
    def impresión(self):
        print(f"""
        VALORES:
        El valor del eje x es: {self.x}
        ------------------------
        El valor del eje y es: {self.y}
        """.strip())
    
    def opuesto(self):
        self.x = -self.x
        self.y = -self.y
        return f"Opuesto de X: {self.x} --- Opuesto de Y: {self.y}"
        
    
prueba_ejes = Punto(5,8)

print(prueba_ejes.eje_x())
print(prueba_ejes.eje_y())
prueba_ejes.impresión()
print(prueba_ejes.opuesto())
prueba_ejes.impresión()
