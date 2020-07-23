#Herencia Multiple
class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("llamando . . . ")
    def ocupado(self):
        print("ocpado . . .")

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print("tomando fotos..")

class Reproduccion:
    def __init__(self):
        pass
    def reproducciondemusica(self):
        print("reproducir musica")
    def reproducirvideo(self):
        print("reproducir un video")

class smartphone(Telefono, Camara, Reproduccion):
    def __del__(self): #este metodo es para limpiar recursos (destructor)
        print("telefono apagado")

movil = smartphone()
print(dir(movil)) #nos da las funciones que podemos usar
print(movil.llamar())

