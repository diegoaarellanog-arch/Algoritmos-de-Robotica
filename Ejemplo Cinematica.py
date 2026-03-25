from roboticstoolbox import *
from spatialmath.base import *
import math

h1 = 0.5
l1 = 10
l2 = 10
l3 = 2.5

q1 = 0
q2 = 0

R = []
R.append(RevoluteDH(d=h1, alpha=0, a=0, offset=0, qlim=[0, math.pi]))
R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0, qlim=[0, math.pi]))
R.append(PrismaticDH(theta=0, alpha=np.pi, a=l2, offset=l3, qlim=[0,2.5]))

Robot = DHRobot(R, name='Robito')
print(Robot)

Robot.teach([q1, q2, q3, q4], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2,q3,q4])
print(MTH)
print(f'Roll, Pitch, Yaw = {tr2rpy(MTH.R, 'deg', 'zyx')}')