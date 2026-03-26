from sympy import *
import numpy
import sympy as sp
from spatialmath.base import *
# from scipy.spatial.transform import Rotation as R

def RotarZ(q):
    """Genera una matriz de rotación en Z compatible con SymPy (Simbólico)"""
    return sp.Matrix([[sp.cos(q), -sp.sin(q), 0, 0],
                      [sp.sin(q),  sp.cos(q), 0, 0],
                      [0,          0,         1, 0],
                      [0,          0,         0, 1]])

theta1, theta2, a1, a2, a3, a4, d3 = symbols('theta1 theta2 a1 a2 a3 a4 d3')

##
# Geometrico
##

Rx = numpy.array([[1, 0,  0],
                  [0, -1, 0],
                  [0, 0,  -1]])
Rz = numpy.array([[cos(theta1+theta2), -sin(theta1+theta2), 0],
                  [sin(theta1+theta2),  cos(theta1+theta2), 0],
                  [                 0,                   0, 1]])

Rxz = numpy.matmul(Rz,Rx)
print(f'Rxz = {Rxz}')

##
# Transformaciones
##

# theta1 = pi/2
# theta2 = pi/2
# l1 = 5
# l2 = 5
# h1 = 3
# h2 = 2

T01 = numpy.array([[1, 0, 0,  0],
                   [0, 1, 0,  0],
                   [0, 0, 1, a1],
                   [0, 0, 0,  1]])

T12 = numpy.array([[cos(theta1), -sin(theta1), 0, a2*cos(theta1)],
                   [sin(theta1), cos(theta1), 0, a2*sin(theta1)],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

T23 = numpy.array([[cos(theta2), -sin(theta2), 0, a3*cos(theta2)],
                   [sin(theta2), cos(theta2), 0, a3*sin(theta2)],
                   [0, 0, -1, 0],
                   [0, 0, 0, 1]])

   
T34 = numpy.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, d3+a4],
                   [0, 0, 0, 1]])

T02 = numpy.matmul(T01,T12)
T24 = numpy.matmul(T23,T34)
T04 = simplify(numpy.matmul(T02,T24))
# T04 = (numpy.matmul(T02,T24))
print(f'T04 = {T04}')

# r = T04[:3,:3]
# print(f'r = {r}')
# print(f'Roll, Pitch, Yaw = {tr2rpy(r, 'deg', 'zyx')}')

#-------------Opción 2 (scipy.spatial.transform)-------------
# r = R.from_matrix(T04[:3,:3])
# print(f'r = {r}')
# # m = numpy.rad2deg(tr2rpy(r,'zyx'))
# m = r.as_euler('zyx', degrees=True)
# print(f'm = {m}')