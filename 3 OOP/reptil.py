class Reptil:
    def __init__(self, nombre):
        self.nombre = nombre
        
class Serpiente(Reptil):
    pass

class Culebra(Serpiente):
    pass

Reptil1 = Reptil("Lagarto")
Serpiente1 = Serpiente("Mamba negra")
Culebra1 = Culebra("Culebra ibérica")

print(Reptil.__name__)
print(type(Serpiente1).__name__)
print(type(Culebra1).__name__)


print(f"\t\t{Reptil.__name__}\t{Serpiente.__name__}\t{Culebra.__name__}")
for cls1 in [Reptil, Serpiente, Culebra]:
    print(cls1.__name__ ,end="\t")
    for cls2 in [Reptil,Serpiente, Culebra]:
        print(issubclass(cls1, cls2), end="\t")
        print()
        
print(f"\t\t{type(Reptil1).__name__}\t{type(Serpiente1).__name__}\t{type(Culebra1).__name__}")

for obj in [Reptil1, Serpiente1, Culebra1 ]:
    print(obj.nombre, end="\t")
    for clase in [Reptil, Serpiente, Culebra]:
        print(isinstance(obj, clase), end="\t")
    print()
    
    
Reptil_1 = Reptil("Rana")
Reptil_2 = Reptil("Vibora")
Reptil_3 = Reptil("Cocodrilo")

Reptil_1 = Reptil_2
Reptil_2 = Reptil_3
Reptil_1 = Reptil_3

print(Reptil_1 == Reptil_2, Reptil_2 is Reptil_1)
print(Reptil_2 == Reptil_3, Reptil_2 is Reptil_3)
print(Reptil_1 == Reptil_3, Reptil_1 is Reptil_3)
