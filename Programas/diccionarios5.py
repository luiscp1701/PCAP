
asignaturas = {
        'Matemáticas': 6,
        'Física': 4,
        'Química': 5
    }

total_creditos = 0

for asignatura, creditos in asignaturas.items():
        print(f"{asignatura} tiene {creditos} créditos.")
        total_creditos += creditos

print(f"El número total de créditos del curso es: {total_creditos}")
