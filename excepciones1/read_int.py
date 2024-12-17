def read_int(prompt, min, max):
    while True:
        try:
            valor = int(input(prompt))
            if (valor>=-10 and valor<=10):
                return valor
        except ValueError:
            print("ingresa un número correcto")
        except:
            print("error terrorifico")
                 
v = read_int("Ingresa un númeor entre -10 a 10: ", -10, 10)
    
print("El número es:", v)