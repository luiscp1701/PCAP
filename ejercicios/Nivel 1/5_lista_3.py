def numeros_ganadores():
    numeros = []
    for i in range(6):
        numero = int(input(f"Introduce el número ganador {i+1}: "))
        numeros.append(numero)
    numeros.sort()
    print("Números ganadores ordenados:", numeros)


numeros_ganadores()