#Esto es el ocultamiento de datos del estado interno
#para proteger la integridad del objeto
## uso dos rayas bajas delante del atributo
class Cliente:
    def __init__(self):
        self.__codigo = 4321

    def __cuenta(self):
        print("Cuenta de procesamiento")

    def getcodigo(self):
        return self.__codigo

persona = Cliente()

#para llamarlo necesito:
# #objeto._nombreclase__nombre atributo
print(persona._Cliente__codigo)
persona._Cliente__cuenta()
