#f-strings
#format %
#str.format

#comenzamos a ver Polimorfismo

#curso = "python"
#nombre = "koki"
#edad = 22
# %

#Repaso
#print("Tutoriales de % s" %curso)
#output:Tutoriales de python

#print("Hechos por % s y tengo % s años"%(nombre, edad))
#output: Hechos por koki y tengo 22 años

# str.format
#print("Espero les guste el curso de {}, yo soy {}, y tengo {}". format(curso,nombre,edad))
#output: Espero les guste el curso de python, yo soy koki, y tengo 22

#f.strings python 3.6
#print(f"hola soy {nombre} y mi edad es {edad}")
#output: hola soy koki y mi edad es 22
# A partir de aca vamos comenzamos a hacer un ejercicio usando f.string

class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):#Representacion informal de una cadena de caracteres
        #es decir el metodo __str__ no esta pensado para
        #ser ejectudo ni interpretado por el codigo
        #visualizacion inmediata
        return f"Hola, ¿que tal?, soy {self.nombre} {self.apellido} y tengo {self.edad} años"

    def __repr__(self): #funciona como el str, pero si se ejecuta con el codigo
        return f"Hola, ¿que tal?, soy {self.nombre} {self.apellido} y tengo {self.edad} años"

nuevo_estudiante= Estudiante("koki", "orba", 22)
print(f"{nuevo_estudiante}")
#aca usamos __repr__
print(f"{nuevo_estudiante !r}")
