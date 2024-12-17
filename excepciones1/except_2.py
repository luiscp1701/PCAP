try:
    y=1/10
 
# Excepción de dos tipos
except (ZeroDivisionError, ArithmeticError):
    print("Hubo un problema al hacer la operación.")
 

 
# Excepción para cualquier otro problema.
except:
    print("Algo ha cascao aqui...")
   
print("FIN")