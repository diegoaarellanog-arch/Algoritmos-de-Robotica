clear all
close all
clc

l1 = 10;
l2 = 8;
l3 = 5;
l4 = 5;

q1 = 0;
q2 = 0;
q3 = 0;

R(1) = Link('revolute','d',0,'alpha',0,'a',l2,'offset',0);
R(2) = Link('revolute','d',0,'alpha',pi,'a',l3,'offset',0);
R(3) = Link('prismatic','theta',0,'alpha',0 ...
    va,'a',0,'offset',l4);
R(3).qlim = [0,10];


Robot = SerialLink(R,'name','Bender')

Robot.plot([q1,q2, q3],'scale',1.0,'workspace',[-30 30 -30 30 -30 30]);
zlim([-15,30]);
Robot.teach([q1,q2,q3],'rpy/zyx');
MTH = Robot.fkine([q1,q2,q3])
fprintf('Roll, Pitch, Yaw = [%.3f %.3f %.3f] \n',rad2deg(tr2rpy(MTH.R,'zyx')));