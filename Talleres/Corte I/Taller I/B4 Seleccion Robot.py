# ----------------   Librerias   ---------------- #
import numpy as np

# ----------------      Main      ----------------#
opc = input('Robots disponibles: \n1. Robot Cilindrico \n2. Robot Cartesiano \n3. Robot Esférico \n\n¿Qué robot desea utilizar? (1/2/3) \n >> ')

while True:
    if opc == '1':
        print('Robot Cilíndrico seleccionado')
        break
    elif opc == '2':
        print('Robot Cartesiano seleccionado')
        break
    elif opc == '3':
        print('Robot Esférico seleccionado')
        break
    else:
        opc = input('Opción no válida, por favor seleccione una opción del 1 al 3\n >> ')