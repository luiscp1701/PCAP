def jugar():
    opciones = ["piedra", "papel", "tijera"]
    while True:
        jugador = input("Elige piedra, papel o tijera: ").strip().lower()
        if jugador not in opciones:
            print("Opción no válida. Intenta de nuevo.")
            continue
        maquina = random.choice(opciones)
        print(f"La máquina eligió: {maquina}")
        if jugador == maquina:
            print("Empate")
        elif (jugador == "piedra" and maquina == "tijera") or \
             (jugador == "papel" and maquina == "piedra") or \
             (jugador == "tijera" and maquina == "papel"):
            print("Ganaste")
        else:
            print("Perdiste")
        otra_vez = input("Quieres jugar de nuevo? (s/n): ").strip().lower()
        if otra_vez != "s":
            break


jugar()