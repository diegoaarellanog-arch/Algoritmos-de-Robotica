import numpy as np
import math

R0 = 100.0
#Coeficientes definidos por la norma IEC 60751
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12
T = 100.0 # Ejemplo a 100°C

if T <= 0:
    resistencia = R0 * (1 + A * T + B * T**2)
else:
    C = -4.183e-12
    resistencia = R0 * (1 + A * T + B * T**2 + C * (T - 100) * T**3)

print("--- 4. PT100 💍--- \n") 
print("Platino (PT) a los 100 ohmios está a exactamente 0°C \n")
print(f"Resistencia a {T}°C: {resistencia:.2f} Ω\n")
