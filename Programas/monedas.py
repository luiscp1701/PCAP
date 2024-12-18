monedas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

moneda = input("Introduce el nombre de una moneda (Euro, Dollar, Yen): ").title()

if moneda in monedas:
        print(f"El símbolo de la moneda {moneda} es: {monedas[moneda]}")
else:
        print("La moneda no existe aquí.")


