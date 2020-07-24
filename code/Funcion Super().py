#La funcion super() se utiliza para llamar a metodos definidos
#me ayuda a darle mas enfasis a una clase secundaria

class Mamimefero:
    def __init__(self, nombre):
        print(nombre, "es un animal de sangre caliente")
class Leon(Mamimefero):
    def __init__(self):
        print("el leon es un animal de 4 patas")
        super().__init__("Simba")
nuevo_leon = Leon()