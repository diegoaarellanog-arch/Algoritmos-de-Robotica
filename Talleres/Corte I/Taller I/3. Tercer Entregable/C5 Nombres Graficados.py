#Dibuje el nombre de cada uno de los integrantes del grupo en un plot en 2D, teniendo en cuenta líneas rectas y/o curvas

import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4, 1, figsize=(8,8))

def A(x):
    plt.plot([x, x+0.5], [0, 2])
    plt.plot([x+0.5, x+1], [2, 0])
    plt.plot([x+0.25, x+0.75], [1, 1])

def C(x):
    plt.plot([x, x], [0, 2])
    plt.plot([x, x+1], [2, 2])
    plt.plot([x, x+1], [0, 0])

def D(x):
    plt.plot([x, x], [0, 2])
    plt.plot([x, x+0.8], [2, 2])
    plt.plot([x, x+0.8], [0, 0])
    plt.plot([x+0.8, x+0.8], [0, 2])

def E(x):
    plt.plot([x, x], [0, 2])
    plt.plot([x, x+1], [2, 2])
    plt.plot([x, x+1], [1, 1])
    plt.plot([x, x+1], [0, 0])

def F(x):
    plt.plot([x, x], [0, 2])
    plt.plot([x, x+1], [2, 2])
    plt.plot([x, x+0.8], [1, 1])

def G(x):
    plt.plot([x, x], [0, 2])
    plt.plot([x, x+1], [2, 2])
    plt.plot([x, x+1], [0, 0])
    plt.plot([x+1, x+1], [0, 1])
    plt.plot([x+0.5, x+1], [1, 1])

def I(x):
    plt.plot([x+0.5, x+0.5], [0, 2])
    plt.plot([x, x+1], [2, 2])
    plt.plot([x, x+1], [0, 0])

def J(x):
    plt.plot([x+1, x+1], [2, 0])
    plt.plot([x+0.3, x+1], [0, 0])
    plt.plot([x+0.3, x+0.3], [0, 0.5])

def L(x):
    plt.plot([x, x], [0, 2])
    plt.plot([x, x+1], [0, 0])

def M(x):
    plt.plot([x, x], [0, 2])
    plt.plot([x+1, x+1], [0, 2])
    plt.plot([x, x+0.5], [2, 0])
    plt.plot([x+0.5, x+1], [0, 2])

def N(x):
    plt.plot([x, x], [0, 2])
    plt.plot([x+1, x+1], [0, 2])
    plt.plot([x, x+1], [2, 0])

def O(x):
    plt.plot([x, x], [0, 2])
    plt.plot([x+1, x+1], [0, 2])
    plt.plot([x, x+1], [2, 2])
    plt.plot([x, x+1], [0, 0])

def P(x):
    plt.plot([x, x], [0, 2])
    plt.plot([x, x+1], [2, 2])
    plt.plot([x+1, x+1], [1, 2])
    plt.plot([x, x+1], [1, 1])

def R(x):
    P(x)
    plt.plot([x, x+1], [1, 0])

def U(x):
    plt.plot([x, x], [0, 2])
    plt.plot([x+1, x+1], [0, 2])
    plt.plot([x, x+1], [0, 0])

def Y(x):
    plt.plot([x, x+0.5], [2, 1])
    plt.plot([x+1, x+0.5], [2, 1])
    plt.plot([x+0.5, x+0.5], [1, 0])

def Z(x):
    plt.plot([x, x+1], [2, 2])
    plt.plot([x+1, x], [2, 0])
    plt.plot([x, x+1], [0, 0])


def escribir(nombre):
    dic = {
        'A': A, 'C': C, 'D': D, 'E': E, 'F': F,
        'G': G, 'I': I, 'J': J, 'L': L, 'M': M,
        'N': N, 'O': O, 'P': P, 'R': R, 'U': U, 
        'Y': Y, 'Z': Z
    }

    x = 0
    for letra in nombre:

        if letra == " ":        
            x += 2

        elif letra in dic:
            dic[letra](x)
            x += 1.5

# Nombre 1
plt.sca(axs[0])   # Cambiamos al primer subplot
escribir("DIEGO ARELLANO")
axs[0].set_aspect('equal')
axs[0].axis('off')
axs[0].set_title("Primer Integrante")


# Nombre 2
plt.sca(axs[1])
escribir("JUAN CARRILLO")
axs[1].set_aspect('equal')
axs[1].axis('off')
axs[1].set_title("Segundo Integrante")


# Nombre 3
plt.sca(axs[2])
escribir("JEAN PIERRE FAJARDO")
axs[2].set_aspect('equal')
axs[2].axis('off')
axs[2].set_title("Tercer Integrante")

# Nombre 4
plt.sca(axs[3])
escribir("MARLLY RODRIGUEZ")
axs[3].set_aspect('equal')
axs[3].axis('off')
axs[3].set_title("Cuarto Integrante")


plt.tight_layout()
plt.show()