syms theta1 theta2
RZ1 = simplify(RotarZ(theta1)*RotarZ(theta2))
RZ2 = simplify(RotarZ(theta2)*RotarZ(theta1))
RZ3 = simplify(RotarZ(theta1+theta2))