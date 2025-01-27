class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed+ " dice: ¡Guau!"
    
class SheepDog(Dog):
    def __str__(self):
        return super().__str__()+ " ¡No huyas corderito!"
    
class GuardDog(SheepDog):
    def __str__(self):
        return super().__str__()+ " ¡Quedese donde esta, intruso!"
    
    
class LowLandDog(SheepDog):
    def __str__(self):
        return super().__str__()+ "  Guau, soy un perro de la hostia!"
    
rocky = SheepDog("Collie")
luna = GuardDog("Doberman")
francisco = LowLandDog("Mil leches")

print(rocky)
print(luna)
print(francisco)

print(issubclass(SheepDog, Dog)), issubclass(SheepDog, GuardDog)
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))