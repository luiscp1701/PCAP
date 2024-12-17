try:
    y=1/10
 
# Excepción más concreta
except ZeroDivisionError:
    print("División entre cero no disponible")
 
# Excepción más abstracta/general
except ArithmeticError:
    print("Problema aritmético")
 
# Excepción para cualquier otro problema.
except:
    print("Algo ha cascao aqui...")
   
print("FIN")