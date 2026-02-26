# 2. Realice un programa que le permita al usuario ingresar los coeficientes de una función de transferencia de 
# segundo orden y graficar su comportamiento, además se debe mostrar que tipo de sistema es: subamortiguado, criticamente
# amortiguado y sobreamortiguado.

# -------- Librerías --------
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# -------- Configuración --------
np.set_printoptions(precision=4, suppress=True)

# -------- Entrada de datos --------
print("Sistema de Segundo Orden")
b0 = float(input("Ingrese b0 (numerador): "))

a2 = float(input("Ingrese a2: "))
a1 = float(input("Ingrese a1: "))
a0 = float(input("Ingrese a0: "))

# -------- Cálculo parámetros dinámicos --------
wn = np.sqrt(a0 / a2)
zeta = a1 / (2 * np.sqrt(a0 * a2))

# -------- Clasificación --------
if zeta < 1:
    tipo = "Subamortiguado"
elif np.isclose(zeta, 1):
    tipo = "Críticamente amortiguado"
else:
    tipo = "Sobreamortiguado"

# -------- Sistema --------
num = [b0]
den = [a2, a1, a0]

sistema = signal.TransferFunction(num, den)

# -------- Respuesta al escalón --------
t, y = signal.step(sistema)

# -------- Gráfica --------
plt.figure()
plt.plot(t, y)
plt.title(f"Respuesta al Escalón\nTipo: {tipo}")
plt.xlabel("Tiempo (s)")
plt.ylabel("Respuesta")
plt.grid(True)
plt.show()

# -------- Resultados --------
print("\nFrecuencia natural (wn):", round(wn,4))
print("Factor de amortiguamiento (zeta):", round(zeta,4))
print("Tipo de sistema:", tipo)