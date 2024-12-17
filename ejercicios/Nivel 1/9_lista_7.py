def contar_vocales():
    palabra = input("Introduce una palabra: ").strip().lower()
    vocales = "aeiou"
    conteo = {vocal: palabra.count(vocal) for vocal in vocales}
    print("Número de veces que aparece cada vocal:")
    for vocal, cantidad in conteo.items():
        print(f"{vocal}: {cantidad}")

contar_vocales()