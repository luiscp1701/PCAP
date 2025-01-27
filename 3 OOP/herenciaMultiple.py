class Saiyan:
    planeta = "Sadala"
    def __init__(self, nombre):
        self.nombre = nombre
        
class Humano:
    planeta = "Tierra"
    def __init__(self, nombre):
        self.nombre = nombre
        
class Mestizo(Saiyan, Humano):
    def __init__(self, nombre, a , b):
        self.nombre = nombre
        self.padre = a.nombre
        self.madre = b.nombre
        
        def verAncestros(self):
            for ancestro in Mestizo.__bases__:
                print(ancestro.__name__, end=' ')
                print()

goku = Saiyan("Son Goku")
vegeta = Saiyan("Vegeta")
bulma = Humano("Bulma")
trunks = Mestizo("Trunks",vegeta, bulma)

print(type(trunks).__name__)
print(type(goku).__name__)
print(type(vegeta).__name__)
print(type(bulma).__name__)

print (trunks.__dict__)
print(f"El padre de {trunks.nombre} es {trunks.__dict__['padre']}")


print(trunks.planeta)
trunks.planeta = "Tierra"
print(trunks.planeta)

if type(trunks).__name__ == "Mestizo":
    if issubclass(Mestizo,Saiyan):
        print(f"{trunks.nombre} puede convertirse en supersaiyan")
        if issubclass(Mestizo, Humano):
            print(f"{trunks.nombre} tiene madre humana")
    else:
        print(f"{trunks.nombre} NO puede convertirse en supersaiyan")