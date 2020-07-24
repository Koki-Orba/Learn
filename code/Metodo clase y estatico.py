import math

class Pastel:
    def __init__(self, ingredientes, tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño

    def __repr__(self):
        return (f"Pastel({self.ingredientes}, 'f'{self.tamaño})")


    #Metodo clase
    #Los CLS me ayuda a decir que son idependientes pero que pertenecen a una clase
#    @classmethod
#    def Pastel_chocolate(cls):
#        return cls(["harina", "leche", "chocolate"])
#    @classmethod
#    def Pastel_vainilla(cls):
#        return cls(["harina", "leche", "vainilla"])
#
# print(Pastel.Pastel_chocolate()) #Metodo clase
#
# Comentamos el metodo clase para que funcione el metodo estatico

    # Metodo Estatico

    def area(self):
        return self.tamaño_area(self.tamaño)
    @staticmethod

    def tamaño_area(A): # A = área
        return A ** 2 * math.pi

nuevo_pastel = Pastel(["harina", "azucar", "leche", "crema"], 4)
print(nuevo_pastel.tamaño_area(12)) # recordemos que el metodo estatico trabaja independiente




