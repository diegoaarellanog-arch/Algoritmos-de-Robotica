import numpy as np

ARROZ = np.array([3,7,4])
POLLO = np.array([6,3,7])

SUMA=ARROZ+POLLO
RESTA=ARROZ-POLLO
PUNTO=ARROZ@POLLO
CRUZ= np.cross(ARROZ, POLLO)
DIV=ARROZ/POLLO

print("--- 1. VECTORSITOS ---\n")
print("LA SUMA ES: ", SUMA)
print("LA RESTA ES: ", RESTA)
print("LA PUNTO ES: ", PUNTO)
print("LA CRUZ ES: ", CRUZ)
print("LA DIVISION DE LOS VECTORES ES: ", DIV)