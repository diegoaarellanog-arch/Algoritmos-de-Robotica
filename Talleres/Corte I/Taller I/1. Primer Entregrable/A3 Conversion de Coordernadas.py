import math

# Rectangulares
X, Y, Z = 3, 4, 5

# Cilíndricas
RADIO = math.sqrt(X**2 + Y**2)
ANGU = math.atan2(Y, X)

# Esféricas
R_ESF = math.sqrt(X**2 + Y**2 + Z**2)
THETA = math.acos(Z / R_ESF)

print("--- 3. COORDENADITAS ---\n")
print(f"Cilíndricas: \n Radio={RADIO:.2f}, Ángulo={math.degrees(ANGU):.2f}°, z={Z}\n")
print(f"Esféricas: \n Radio={R_ESF:.2f}, Ángulo={math.degrees(THETA):.2f}°, Phi={math.degrees(ANGU):.2f}°\n")

