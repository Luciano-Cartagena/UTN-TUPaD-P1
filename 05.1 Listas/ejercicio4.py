#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
#respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
#en los videos o bien investigar cómo funciona el indexing con números negativos! 
#animales = ["perro", "gato", "conejo", "pez"] 

# Creamos la lista inicial con cuatro animales
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazamos el segundo valor (índice -3 equivale a índice 1 → "gato") por "loro"
animales[-3] = "loro"

# Reemplazamos el último valor (índice -1 → "pez") por "oso"
animales[-1] = "oso"

# Imprimimos la lista resultante
print(animales)
