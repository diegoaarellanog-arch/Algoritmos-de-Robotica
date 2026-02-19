import numpy as np
import matplotlib.pyplot as plt

def resistencia_pt100(T):
    R0 = 100.0
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12
    
    # Aplicar fórmula según el rango de temperatura
    if T >= 0:
        return R0 * (1 + A * T + B * T**2)
    else:
        return R0 * (1 + A * T + B * T**2 + C * (T - 100) * T**3)

# Crear vector de temperaturas de -200 a 200
temperaturas = np.linspace(-200, 200, 400)
# Calcular resistencias (vectorizado)
resistencias = np.array([resistencia_pt100(t) for t in temperaturas])

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(temperaturas, resistencias, label='Curva PT100 (DIN/IEC 60751)', color='red', linewidth=2)

# Detalles del gráfico
plt.title('Comportamiento del Sensor PT100 (-200°C a 200°C)')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ω)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(100, color='black', linewidth=0.8, linestyle='--') # Línea en 100 ohms
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')   # Línea en 0 grados
plt.legend()

# Mostrar puntos clave
plt.annotate(f'100Ω a 0°C', xy=(0, 100), xytext=(20, 80),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()