import random

def adivina_un_intento():
    numero = 7
    intento = int(input("Adivina el número (tienes 1 intento): "))
    if intento == numero:
        print("¡Correcto!")
    else:
        print("Incorrecto. El número era", numero)

def adivina_diez_intentos():
    numero = 7
    for i in range(10):
        intento = int(input(f"Intento {i+1}/10: Adivina el número: "))
        if intento == numero:
            print("¡Correcto!")
            return
        else:
            print("Incorrecto.")
    print("Se acabaron los intentos. El número era", numero)

def adivina_sin_limite():
    numero = 7
    while True:
        intento = int(input("Adivina el número: "))
        if intento == numero:
            print("¡Correcto!")
            break
        else:
            print("Incorrecto, intenta de nuevo.")


tipo = input("Elige versión (A, B o C): ").strip().upper()
if tipo == "A":
    adivina_un_intento()
elif tipo == "B":
    adivina_diez_intentos()
elif tipo == "C":
    adivina_sin_limite()