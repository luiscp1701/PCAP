def abecedario_sin_multiplos_de_tres():
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    resultado = [letra for i, letra in enumerate(abecedario, start=1) if i % 3 != 0]
    print("Abecedario sin letras en posiciones múltiplos de 3:", resultado)


abecedario_sin_multiplos_de_tres()