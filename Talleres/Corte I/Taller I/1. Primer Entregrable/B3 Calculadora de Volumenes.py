#3. Realice un programa para el cálculo de volúmenes (Prisma, Pirámide, Cono truncado, Cilindro) donde el usuario pueda seleccionar
# el sólido y los parámetros de cada volumen.

import numpy as np

# Funciones para el cálculo de los volumenes 
def volumen_prisma(area_base, altura):
    return area_base * altura

def volumen_piramide(area_base, altura):
    return (1/3) * area_base * altura

def volumen_cilindro(radio, altura):
    return np.pi * radio**2 * altura

def volumen_cono_truncado(R, r, altura):
    return (1/3) * np.pi * altura * (R**2 + r**2 + R*r)

# Menú de selección del sólido
print("Cálculo de Volúmenes")
print("1. Prisma")
print("2. Pirámide")
print("3. Cilindro")
print("4. Cono Truncado")

# Entrada del usuario
opcion = int(input("Seleccione el sólido (1-4): "))

# Ingreso de parametros
if opcion == 1:
    A = float(input("Ingrese el área de la base: "))
    h = float(input("Ingrese la altura: "))
    V = volumen_prisma(A, h)

elif opcion == 2:
    A = float(input("Ingrese el área de la base: "))
    h = float(input("Ingrese la altura: "))
    V = volumen_piramide(A, h)

elif opcion == 3:
    r = float(input("Ingrese el radio: "))
    h = float(input("Ingrese la altura: "))
    V = volumen_cilindro(r, h)

elif opcion == 4:
    R = float(input("Ingrese el radio mayor: "))
    r = float(input("Ingrese el radio menor: "))
    h = float(input("Ingrese la altura: "))
    V = volumen_cono_truncado(R, r, h)

else:
    print("Opción inválida")
    V = None

# Resultados
if V is not None:
    print(f"\nEl volumen del sólido es: {V:.2f} unidades cúbicas")