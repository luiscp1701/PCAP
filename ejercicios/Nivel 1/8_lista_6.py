def es_palindromo():
    palabra = input("Introduce una palabra: ").strip().lower()
    if palabra == palabra[::-1]:
        print(f"{palabra} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")

es_palindromo()