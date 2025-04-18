#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))  # Se le pide al usuario que ingrese su edad y se convierte a entero.

# Se evalúa la edad ingresada para determinar la categoría:
if edad < 12: 
    print("Perteneces a la categoria de: Niño.")  # Si es menor de 12, se imprime "Niño".
elif edad >= 12 and edad < 18:
     print("Perteneces a la categoria de: Adolescente.")  # Si tiene entre 12 y 17, se imprime "Adolescente".
elif edad >= 18 and edad < 30:
     print("Perteneces a la categoria de: Adulto/a Joven.")  # Si tiene entre 18 y 29, se imprime "Adulto/a Joven".
elif edad >= 30:
     print("Perteneces a la categoria de: Adulto/a.") # Si tiene 30 o más, se imprime "Adulto/a".