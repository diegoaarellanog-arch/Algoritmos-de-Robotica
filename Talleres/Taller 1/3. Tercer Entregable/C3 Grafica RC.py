#3. Implemente la ecuación de carga y descarga para un circuito RC. El usuario ingresa por el teclado el 
# valor de voltaje (V), capacitancia (10^-6F) y resistencia(ohms). Posteriormente realice en Python la gráfica.

# -------- Librerías --------
import numpy as np
import matplotlib.pyplot as plt

# -------- Configuración --------
np.set_printoptions(precision=4, suppress=True)

# -------- Entrada de datos --------
print("Circuito RC - Carga y Descarga")

V = float(input("Ingrese el voltaje (V): "))
R = float(input("Ingrese la resistencia (Ohms): "))
C_micro = float(input("Ingrese la capacitancia (microFaradios 10^-6 F): "))

# Convertir microfaradios a faradios
C = C_micro * 1e-6

# -------- Parámetros --------
tau = R * C  # Constante de tiempo

# Vector de tiempo (0 a 5 constantes de tiempo)
t = np.linspace(0, 5*tau, 1000)

# -------- Ecuaciones --------
Vc_carga = V * (1 - np.exp(-t/tau))
Vc_descarga = V * np.exp(-t/tau)

# -------- Gráfica --------
plt.figure()

plt.plot(t, Vc_carga, label="Carga")
plt.plot(t, Vc_descarga, label="Descarga")

plt.title("Respuesta de un Circuito RC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje en el capacitor (V)")
plt.grid(True)
plt.legend()

plt.show()

# -------- Resultados --------
print("\nConstante de tiempo (tau = RC):", round(tau,6), "segundos")