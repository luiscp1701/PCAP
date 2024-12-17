def ordena_positivos(lista):
    positivos = sorted([num for num in lista if num > 0])
    resultado = []
    
    indice_positivos = 0
    for num in lista:
        if num > 0:
            resultado.append(positivos[indice_positivos])
            indice_positivos += 1
        else:
            resultado.append(num)
    return resultado

lista = [3, -1, 2, -7, 5, 0, -3]
print("Lista original:", lista)
print("Lista transformada:", ordena_positivos(lista))