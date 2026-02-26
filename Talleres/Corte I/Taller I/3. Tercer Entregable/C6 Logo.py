import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw() 
print("Elige la imagen del logo... ✨")

ruta = filedialog.askopenfilename()

if ruta:
    img = Image.open(ruta).convert('L')
    matriz = np.array(img)

    # Detectamos los píxeles del logo (ajusta el 128 si es necesario)
    filas, columnas = np.where(matriz < 128)

    plt.figure(figsize=(7, 7))
    plt.scatter(columnas, filas, s=1, c='deeppink')
    plt.gca().invert_yaxis()  
    
    plt.title("Contorno del Loguito✨")
    plt.show()

    print(f"Puntos detectados: {len(columnas)}")
    for i in range(min(10, len(columnas))):
        print(f"X: {columnas[i]}, Y: {filas[i]}")
else:
    print("No seleccionaste ninguna imagen xd")