import numpy as np
import math

R0 = 100.0
#Coeficientes definidos por la norma IEC 60751
A = 3.9083e-3
B = -5.775e-7
T = 100.0 # Ejemplo a 100°C

resistencia = R0 * (1 + A * T + B * T**2)

print("--- 4. PT100 💍--- \n") 
print("Platino (PT) a los 100 ohmios está a exactamente 0°C \n")
print(f"Resistencia a {T}°C: {resistencia:.2f} Ω\n")

#5. Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo) y un parámetro de salida (matriz). 
def rotacion_x(angulo):
    rad = math.radians(angulo)
    return np.array([[1, 0, 0],
                     [0, math.cos(rad), -math.sin(rad)],
                     [0, math.sin(rad), math.cos(rad)]])

def rotacion_y(angulo):
    rad = math.radians(angulo)
    return np.array([[math.cos(rad), 0, math.sin(rad)],
                     [0, 1, 0],
                     [-math.sin(rad), 0, math.cos(rad)]])

def rotacion_z(angulo):
    rad = math.radians(angulo)
    return np.array([[math.cos(rad), -math.sin(rad), 0],
                     [math.sin(rad), math.cos(rad), 0],
                     [0, 0, 1]])

print("--- 5. ROTACIÓN ---")
print(f"Matriz X (45°):\n{rotacion_x(45)}\n")