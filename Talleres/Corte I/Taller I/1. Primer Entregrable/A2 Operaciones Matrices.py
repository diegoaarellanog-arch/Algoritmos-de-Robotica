import numpy as np

BOCADILLO = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
QUESO = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

suma_m = BOCADILLO + QUESO 
resta_m = BOCADILLO - QUESO 
punto_m = BOCADILLO @ QUESO  
cruz_m = np.cross(BOCADILLO, QUESO )
div_m = BOCADILLO / QUESO

print("--- 2. MATRICITAS ---\n")
print(f"Suma:\n{suma_m}\n")
print(f"Producto Punto :\n{punto_m}\n")
print(f"Producto Cruz:\n{cruz_m}\n")