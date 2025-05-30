# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

def segundos_a_horas(segundos):
    # Convierte los segundos a horas dividiendo por 3600 (60 seg * 60 min)
    return segundos / 3600

segundos = int(input("Ingresa la cantidad de segundos: "))  # Pide al usuario un número entero de segundos

horas = segundos_a_horas(segundos)  # Llama a la función para convertir

# Muestra el resultado al usuario
print(f"La cantidad de horas son {horas} equivalentes a {segundos} segundos.")

