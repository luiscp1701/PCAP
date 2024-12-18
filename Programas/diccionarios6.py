
informacion_persona = {}

while True:
        clave = input("Introduce el tipo de información que deseas añadir (por ejemplo: nombre, edad, etc.): ")
        valor = input(f"Introduce el valor para {clave}: ")

        informacion_persona[clave] = valor


        print("Contenido actual del diccionario:")
        for c, v in informacion_persona.items():
            print(f"{c}: {v}")

        continuar = input("¿Quieres añadir más información? (Si/No): ").lower()
        if continuar != "si":
            break

print("Diccionario final:")
for c, v in informacion_persona.items():
        print(f"{c}: {v}")

