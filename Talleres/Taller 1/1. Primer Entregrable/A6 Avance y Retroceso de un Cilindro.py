import math

P = 600000  # Presión en Pascales (6 bar)
D_embolo = 0.04   # 40mm diámetro
d_vastago = 0.016 # 16mm diámetro

area_embolo = (math.pi * D_embolo**2) / 4
area_anular = area_embolo - ((math.pi * d_vastago**2) / 4)

f_avance = P * area_embolo
f_retroceso = P * area_anular

print("--- 6. CILINDRO ---")
print(f"Fuerza Avance: {f_avance:.2f} N")
print(f"Fuerza Retroceso: {f_retroceso:.2f} N")