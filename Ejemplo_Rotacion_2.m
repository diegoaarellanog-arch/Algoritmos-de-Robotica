clear all
close all
clc

a = round(RotarZ(pi/2)*RotarY(pi/2))
b = round(RotarY(pi/2)*RotarZ(pi/2))

%Excepción si gira en el mismo eje
c = round(RotarX(pi/2)*RotarX(pi))
d = round(RotarX(pi)*RotarX(pi/2))
e = round(RotarX(pi+pi/2))