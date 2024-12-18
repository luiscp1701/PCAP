precios_frutas = {
        'Manzana': 2.5,
        'Cereza': 3.0,
        'Naranja': 1.8,
        'Uva': 2.2
    }


fruta = input("Introduce el nombre de una fruta: ").title()
kilos = input("Introduce el número de kilos: ")

try:
        kilos = float(kilos)
        if fruta in precios_frutas:
            precio_total = precios_frutas[fruta] * kilos
            print(f"El precio de {kilos} kilos de {fruta} es: {precio_total:.2f} euros.")
        else:
            print("La fruta ingresada no está en el diccionario.")
except ValueError:
        print("Por favor, introduce un número válido para los kilos.")
