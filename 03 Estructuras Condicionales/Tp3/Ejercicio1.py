# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: ")) #Se le pide al usuario que ingrese su edad y se convierte ese valor a entero.
mayor_edad = 18 #Se define una constante (por convención) que representa la mayoría de edad.

if edad > mayor_edad: #e evalúa si la edad ingresada es mayor que 18.
    print("Es mayor de edad.") # Si la condición es verdadera, se muestra el mensaje.