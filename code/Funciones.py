# Funciones para atributos

class Persona:
    edad = 27
    nombre = "victor"
    pais = "Costa Rica"

doctor = Persona()

print("la edad es: ", doctor.edad)

print("La edad es: ", getattr(doctor, "edad"))
#getattr me obtiene el valor de forma directa sin ingresar al atributogit

print("el doctor tiene una edad?", hasattr(doctor, "edad"))
#hasattr me ayuda a identificar si existe o no un atributo


setattr(doctor, "nombre", "hector")
print("Ahora el doctor se llama: ", doctor.nombre)
#Funcion para hacer cambios de valor de un atributo

delattr(Persona, "pais") #Esta funcion sirve para eliminar un atributo
print(doctor.pais)
