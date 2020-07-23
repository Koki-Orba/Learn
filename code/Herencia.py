# ejemplo de herencia
class pokemon: #clase superior (padre)
    pass
    def __init__(self, nombre, tipo):
        #vamos a declarar los atributos
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return "{} es un pokemon de tipo {}".format(self.nombre, self.tipo)

class pikachu(pokemon): #clase inferior (hijo)
    def ataque(self, tipo_ataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipo_ataque)

class charmander(pokemon):
    def ataque(self, tipo_ataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipo_ataque)

# luego de crear las clases hacemos los objetos

nuevo_pokemon = pikachu("boby", "electrico") #los valores que utilizamos son los de la clase padre
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("impacto trueno"))