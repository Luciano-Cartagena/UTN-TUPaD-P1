# Ejercicio 7
# Dados dos sets, mostrar intersección, diferencia simétrica y unión

parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107}

# Aprobaron ambos parciales (intersección)
ambos = parcial1.intersection(parcial2)

# Aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1.symmetric_difference(parcial2)

# Aprobaron al menos uno (unión)
todos = parcial1.union(parcial2)

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos uno:", todos)
