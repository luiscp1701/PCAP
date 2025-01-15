class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario
        
        def get_salario(self):
            return self.__salario
        
        def set_salario(self, salario):
            if salario > 0:
                self.__salario = salario
            else:
                return "El salario debe ser mayor de 0"
            
    def __srt__(self):
        return f"Nombre: {self.nombre}, Cargo: {self.cargo}, Salario: {round(self.get_salario)}"

listaEmpleados =[
Empleado("Luis", "Mamporrero", 200000),
Empleado("Juan", "Presidente", 50000),
Empleado("Pedro", "Gerente", 40000),
Empleado("Maria", "Secretaria", 30000)
]
empleados_vip=[ empleado for empleado in listaEmpleados if empleado.get_salario()>50000]


for e in empleados_vip:
    print(e)
        