#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par".

numero = int(input("Ingrese un número: ")) # Se le pide al usuario que ingrese un número, y se convierte a entero.

if numero % 2 == 0: # Se evalúa si el número es par (si el resto de dividir entre 2 es cero).
    print ("Ha ingresado un número par.") # Si la condición es verdadera, se muestra el mensaje correspondiente.
else:
    print("Por favor, ingrese un número par.") # Si no es par, se muestra un mensaje pidiendo que ingrese uno.