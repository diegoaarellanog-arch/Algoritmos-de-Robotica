import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --------- Entrada de datos ---------
zeta = float(input("Ingrese el factor de amortiguamiento (ζ): "))
wn = float(input("Ingrese la frecuencia natural (ωn): "))
K = float(input("Ingrese la ganancia (K): "))

# --------- Función de transferencia ---------
num = [K * wn**2]
den = [1, 2*zeta*wn, wn**2]

system = signal.TransferFunction(num, den)

# --------- Respuesta al escalón ---------
t, y = signal.step(system)

# --------- Clasificación del sistema ---------
if zeta < 1:
    tipo = "Subamortiguado"
elif zeta == 1:
    tipo = "Críticamente amortiguado"
else:
    tipo = "Sobreamortiguado"

# --------- Gráfica ---------
plt.figure()
plt.plot(t, y)
plt.title(f"Respuesta al escalón\nSistema {tipo}")
plt.xlabel("Tiempo")
plt.ylabel("Salida")
plt.grid()
plt.show()

print("\nTipo de sistema:", tipo)