# Nos ayuda a procesar n elemenos a la vez

class Colombia:
    def capital(self):
        print("Bogota")
    def idioma(self):
        print("Español")

class Francia:
    def capital(self):
        print("paris")
    def idioma(self):
        print("frances")

colombiano = Colombia()
frances = Francia()

for pais in (colombiano, frances):
    pais.capital()
    pais.idioma()