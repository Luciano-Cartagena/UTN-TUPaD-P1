# Ejercicio 4
# Programa para almacenar y consultar números telefónicos

contactos = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    contactos[nombre] = numero

# Consultar un contacto
consulta = input("Ingrese el nombre del contacto a consultar: ")

if consulta in contactos:
    print(f"Número de {consulta}: {contactos[consulta]}")
else:
    print(f"No existe el contacto con nombre {consulta}")
