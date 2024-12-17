def crear_y_agregar_elementos():
    mi_lista = []
    print("Lista vacía creada:", mi_lista)
    
    while True:
        elemento = input("Introduce un elemento para agregar a la lista (o escribe 'salir' para terminar): ").strip()
        if elemento.lower() == 'salir':
            break
        mi_lista.append(elemento)
        print("Elemento agregado. Lista actual:", mi_lista)
    
    print("Lista final:", mi_lista)

# Llamada a la función
crear_y_agregar_elementos()