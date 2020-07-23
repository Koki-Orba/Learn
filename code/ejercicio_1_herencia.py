# Ejemplo practico de herencia

class Calculadora:
    def __init__(self, numero): #constructor
        self.num = numero
        self.datos = [0 for i in range(numero)]

    def ingresardato(self):
        self.datos = [int(input("Ingresar datos" + str(i+1)+ "= ")) for i in range(self.num)]

class Op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def suma(self): #metodo
        a, b = self.datos
        s = a + b
        print("el resultado es: ", s)

    def resta(self): #metodo
        a,b = self.datos
        r = a - b
        print("el resultado es: ", r)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)
    def cuadrada(self):
        import math
        a, = self.datos
        print("el resultado es: ", math.sqrt(a))

#creamos el objeto y le asignamos la clase
ejemplo = Op_basicas()
print(ejemplo.ingresardato())
print(ejemplo.suma())

ejemplo2 = raiz()
print(ejemplo2.ingresardato())
print(ejemplo2.cuadrada())














