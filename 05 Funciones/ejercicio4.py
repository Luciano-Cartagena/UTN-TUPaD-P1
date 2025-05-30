#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.

import math  # Importa la biblioteca math para usar el valor de pi

def calcular_area_circulo(radio):
    # Calcula el área usando la fórmula π * r^2
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    # Calcula el perímetro (circunferencia) usando la fórmula 2 * π * r
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingresa el radio: "))  # Solicita el radio al usuario

# Llama a ambas funciones y guarda los resultados
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Muestra los resultados por pantalla
print(f"El área del círculo es {area} y el perímetro del círculo es {perimetro}")


