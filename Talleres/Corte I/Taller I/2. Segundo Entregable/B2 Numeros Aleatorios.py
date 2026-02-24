#2. Realice un programa que calcule X números aleatorios en un rango determinado por el usuario

import numpy as np

# Ingreso de datos
cantidad = int(input("¿Cuántos números desea generar?: "))
minimo = int(input("Ingrese el valor mínimo del rango: "))
maximo = int(input("Ingrese el valor máximo del rango: "))

# Generación de números enteros aleatorios
numeros = np.random.randint(minimo, maximo + 1, cantidad)

print("\nNúmeros generados:")
print(numeros)