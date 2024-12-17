

def convertir_peso():
    peso = float(input("Introduce tu peso: "))
    unidad = input("\u00bf(K)g o (L)bs? ").strip().upper()
    
    if unidad == "K":
        peso_libras = peso / 0.45
        print(f"Tu peso en libras es: {peso_libras:.2f} lbs")
    elif unidad == "L":
        peso_kilos = peso * 0.45
        print(f"Tu peso en kilogramos es: {peso_kilos:.2f} kg")
    else:
        print("Unidad no reconocida. Por favor, elige 'K' para kilogramos o 'L' para libras.")

convertir_peso()