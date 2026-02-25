#1. Realice un programa que calcule la potencia que consume un circuito ingresando por teclado el valor de corriente y voltaje 

# ---------------------------------------------
# P = V * I
# ---------------------------------------------

# Ingreso de datos
voltaje = float(input("Ingrese el voltaje (V): "))
corriente = float(input("Ingrese la corriente (A): "))

# Cálculo de la potencia
potencia = voltaje * corriente
print(f"\nLa potencia consumida es: {potencia:.2f} W")