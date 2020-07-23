#First excercise with class and objects

class nombre:
    pass

victor = nombre()
maria = nombre()

#un atributo es una caracteristica de nuestro objeto y se declara asi:
#object.atributo = valor

victor.age = 30
victor.sex = "male"
victor.country = "Costa Rica"

maria.age = 25
maria.sex = "female"
maria.country = "Colombia"

print(victor.age)
print(maria.age)