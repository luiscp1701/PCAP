def mal_asunto(n):
    # Genera una  excepción de tipo "división por cero"
    raise ZeroDivisionError

try:
    mal_asunto(0)
except ArithmeticError:
    print("Que ha pasao???")
    
print("EN-FIN.")