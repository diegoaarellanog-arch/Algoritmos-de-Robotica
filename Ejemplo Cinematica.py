from roboticstoolbox import *
from spatialmath.base import *
import math
import numpy as np
import matplotlib.pyplot as plt

# --- 1. PARÁMETROS FÍSICOS ---
l1 = 6
l2 = 7
l3 = 3
l4 = 2

# Valores iniciales de las articulaciones
q1 = 0 # Rotación (rad)
q2 = 0 # Extensión prismática (m/cm)

# --- 2. DEFINICIÓN DEL ROBOT (2 GDL) ---
R = []
# Eslabón 1: Revoluta
R.append(RevoluteDH(d=l1, alpha=math.pi/2, a=l3, offset=math.pi/2))

# Eslabón 2: Prismático
# El offset (l2+l4) define la longitud física inicial del brazo
R.append(PrismaticDH(theta=0, alpha=0, a=0, offset=l2+l4))
R[1].qlim = [0, 10] # Límite de extensión de 0 a 10 unidades

Robot = DHRobot(R, name='Bender_2GDL')

# --- 3. CÁLCULO DE CINEMÁTICA DIRECTA ---
# fkine ahora recibe exactamente 2 valores
MTH = Robot.fkine([q1, q2])

print(">>> Configuración del Robot:")
print(Robot)

print("\n>>> Matriz de Transformación Homogénea (MTH):")
print(MTH)

# Extraemos la rotación para calcular RPY
# Usamos comillas dobles afuera para evitar conflictos con 'deg' y 'zyx'
print(f"Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}")

# --- 4. VISUALIZACIÓN ---
# Ajustamos los límites para que el robot de ~15 unidades se vea bien
# Formato: [x_min, x_max, y_min, y_max, z_min, z_max]
limites_grafica = [-15, 15, -15, 15, 0, 20]

# El comando teach ahora solo recibe los 2 parámetros q1 y q2
Robot.teach([q1, q2], 'rpy/zyx', limits=limites_grafica)

# Mantener la ventana abierta
plt.show()