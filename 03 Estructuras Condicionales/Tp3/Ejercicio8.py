#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. 

# Se pide al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Se muestran las opciones disponibles
print ("Ingrese una opción:")
print ("1. Si quiere su en mayúsculas.")
print ("2. Si quiere su nombre en minúsculas. ")
print ("3. Si quiere su nombre con la primera letra en mayúscula.")

# Se solicita al usuario que elija una opción (como texto)
opcion = input("Ingresa el número de tu opción (1-3): ")

# Si elige la opción 1, se muestra el nombre en mayúsculas
if opcion == "1":
    print("En mayúsculas:", nombre.upper())

    # Si elige la opción 2, se muestra el nombre en minúsculas
elif opcion == "2":
    print("En minúsculas:", nombre.lower())

    # Si elige la opción 3, se muestra el nombre con la primera letra de cada palabra en mayúscula
elif opcion == "3":
    print("Con formato título:", nombre.title())
    
    # Si escribe algo que no es una opción válida
else:
    print("Opción no válida.")

