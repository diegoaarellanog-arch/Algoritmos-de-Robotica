# ----------------   Librerias   ---------------- #
import matplotlib.pyplot as plt
import numpy as np

# ----------------      Main      ----------------#
# 1. Solicitar coordenadas al usuario
x = float(input("Ingresa la coordenada X: "))
y = float(input("Ingresa la coordenada Y: "))
z = float(input("Ingresa la coordenada Z: "))

# 2. Configurar la figura y el sistema 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 3. Dibujar el vector (desde el origen 0,0,0)
# quiver(origen_x, origen_y, origen_z, destino_x, destino_y, destino_z)
ax.quiver(0, 0, 0, x, y, z, color='blue', arrow_length_ratio=0.1)

# 4. Configurar límites de los ejes
limit = max(abs(x), abs(y), abs(z), 1)
ax.set_xlim([-limit, limit])
ax.set_ylim([-limit, limit])
ax.set_zlim([-limit, limit])

# 5. Etiquetas de los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title(f'Vector: [{x}, {y}, {z}]')

# Dibujar rejilla para mejor perspectiva
ax.grid(True)

plt.show()