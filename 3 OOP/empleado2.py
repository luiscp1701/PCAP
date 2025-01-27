class Empleado:
    plantilla = []
    num_empleados = 0

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario
        Empleado.num_empleados += 1
        Empleado.plantilla.append(self)

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        if salario > 0:
            self.__salario = salario
        else:
            return "El salario debe ser mayor de 0"

    def __str__(self):
        return f"Nombre: {self.nombre}, Cargo: {self.cargo}, Salario: {round(self.get_salario())}"

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Empleado('{self.nombre}', '{self.cargo}', {self.__salario})"



listaEmpleados = [
    Empleado("Luis", "Mamporrero", 200000),
    Empleado("Juan", "Presidente", 50000),
    Empleado("Pedro", "Gerente", 40000),
    Empleado("Maria", "Secretaria", 30000)
]

empleados_vip = [empleado for empleado in listaEmpleados if empleado.get_salario() > 50000]


print("Empleados VIP:")
for empleado in empleados_vip:
    print(empleado)


num1 = 7
num2 = 7.0
num3 = 7.5

for num in [num1, num2, num3]:
    if Empleado.is_integer(num):
        print(f"{num} es entero.")
    else:
        print(f"{num} no es entero.")
