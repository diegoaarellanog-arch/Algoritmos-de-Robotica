clear all
close all
clc

l1 = 10;
l2 = 8;
l3 = 5;

q1 = 0;
q2 = 0;

R(1) = Link('prismatic','theta',0,'alpha',0,'a',0,'offset',l2+l4);
R(2) = Link('prismatic','theta',0,'alpha',0,'a',0,'offset',l2+l4);
R(3) = Link('prismatic','theta',0,'alpha',0,'a',0,'offset',l2+l4);
R(2).qlim = [0,10];

Robot = SerialLink(R,'name','Bender')

Robot.plot([q1,q2],'scale',1.0,'workspace',[-30 30 -30 30 -30 30]);
zlim([-15,30]);
Robot.teach([q1,q2],'rpy/zyx');
MTH = Robot.fkine([q1,q2])
fprintf('Roll, Pitch, Yaw = [%.3f %.3f %.3f] \n',rad2deg(tr2rpy(MTH.R,'zyx')));


