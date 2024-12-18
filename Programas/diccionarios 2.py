nombre = input("como te llamas?: ")
edad = input("cuantos años tienes?: ")
direccion = input("donde vives?: ")
telefono = input("cual es tu numero?: ")

usuario = {"nombre": nombre,"edad": edad,"direccion": direccion,"telefono": telefono
    }

print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número es {usuario['telefono']}.")
