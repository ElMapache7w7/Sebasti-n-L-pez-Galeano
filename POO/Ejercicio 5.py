#Escriba un clase padre llamada Ave que herede a clases 
# hijas con tipos de aves
class Ave:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Loro(Ave):
    def __init__(self):
        super().__init__("Loro") 

class Guacamayo(Ave):
    def __init__(self):
        super().__init__("Guacamayo")

class Codorniz(Ave):
    def __init__(self):
        super().__init__("Codorniz")

loro = Loro()
guacamayo = Guacamayo()
codorniz = Codorniz()

print(f"Las aves son: {loro}, {guacamayo}, {codorniz}")
