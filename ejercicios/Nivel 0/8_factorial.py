def factorial():
    numero = int(input("Introduce un número entero positivo: "))
    if numero < 0:
        print("El número debe ser positivo")
        return
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    print(f"El factorial de {numero} es: {resultado}")


factorial()