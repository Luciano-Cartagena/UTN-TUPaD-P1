# Ejercicio 6
# Ingresar nombres de 3 alumnos y sus 3 notas, mostrar promedio por alumno

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

# Calcular y mostrar promedios
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {alumno}: {promedio:.2f}")
