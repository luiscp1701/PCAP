def mal_asunto(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise #regenera la excepcion

try:
    mal_asunto(0)
except ArithmeticError:
    print("Ya veo!")
    exit(0)
    
    
print ("EN_FIN")