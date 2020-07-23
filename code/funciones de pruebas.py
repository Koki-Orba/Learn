class Calculadora:
    def __init__(self, numero): #constructor
        self.num = numero
        self.datos = [0 for i in range(numero)]

    def ingresardato(self):
        self.datos = [int(input("Ingresar datos" + str(i+1)+ "= ")) for i in range(self.num)]

class op_basicas(Calculadora):
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

#Funcion de prueba
object = op_basicas()
print(isinstance(object, op_basicas) )# Verificamos la herencia, (si el objeto esta en esa clase)
print(issubclass(op_basicas, Calculadora)) #verificamos herencia de clases (hijo, padre)