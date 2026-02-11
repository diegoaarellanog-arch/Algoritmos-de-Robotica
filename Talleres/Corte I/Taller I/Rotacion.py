# ----------------   Librerias   ---------------- #
import numpy as np

# ---------------- Configuracion ---------------- #
np.set_printoptions(suppress = True, precision = 4)

# ----------------   Variables   ---------------- #

POS = np.array([0, 1, 0])
# ----------------   Funciones   ---------------- #
def RotX(deg): # Rotacion en x
    Rx = np.array([[1, 0, 0], [0, np.cos(deg), -np.sin(deg)], [0, np.sin(deg), np.cos(deg)]])
    Res = np.dot(Rx, POS)
    return Res

def RotY(deg): # Rotacion en y
    Ry = np.array([[np.cos(deg), 0, np.sin(deg)], [0, 1, 0], [-np.sin(deg), 0, np.cos(deg)]])
    Res = np.dot(Ry, POS)
    return Res

def RotZ(deg): # Rotacion en z
    Rz = np.array([[np.cos(deg), -np.sin(deg), 0], [np.sin(deg), np.cos(deg), 0], [0, 0, 1]])
    Res = np.dot(Rz, POS)
    return Res

# ----------------      Main      ----------------#

ang = np.pi/2
print(f'{POS} rotado en X {ang * 180/np.pi} grados: {RotX(ang)}')
print(f'{POS} rotado en Y {ang * 180/np.pi} grados: {RotY(ang)}')
print(f'{POS} rotado en Z {ang * 180/np.pi} grados: {RotZ(ang)}')