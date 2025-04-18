#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: ")) # Se le pide al usuario que ingrese su nota, y se convierte a número entero.
nota_aprobado = 6 # Se define el valor mínimo para aprobar (en este caso, 6).

if nota >= nota_aprobado: # Se evalúa si la nota es mayor o igual a 6.
    print("Aprobado.")  # Si la condición es verdadera, se muestra "Aprobado".
else:
    print("Desaprobado.") # Si la condición es falsa (nota menor a 6), se muestra "Desaprobado".
