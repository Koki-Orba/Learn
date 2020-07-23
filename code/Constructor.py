#Metodos Constructores

class Persona:
    pass #funciona para dar a entender que por ahora no se declaran atributos
    #__init__ es un constructor
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año

    # ahora haremos un metodo
    def descripcion(self):
        return " {} tiene {}".format(self.nombre, self.año)

    def comentario(self, frase):
        return "{}, dice {} años".format(self.nombre, frase)

#crearemos un objeto a continuación
doctor = Persona("José", 26)
print(doctor.descripcion())
print(doctor.comentario("hola que tal"))




# ejercicio 2
# modificar un atributo
class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()
print(mi_correo.enviado)

#Vamos a acceder al otro atributo
mi_correo.enviar_correo()
print(mi_correo.enviado)



