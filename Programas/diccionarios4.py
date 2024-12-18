meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")

dia, mes, año = fecha.split("/")
mes = int(mes) 

if 1 <= mes <= 12:
    print(f"{dia} de {meses[mes - 1]} de {año}")
else:
    print("El mes ingresado no es válido.")