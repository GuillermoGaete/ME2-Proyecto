%% 
clc;
clear;
 d = dipole;
[efield,az,el] = pattern(d, 75e6,'Type','efield');
phi = az';
theta = (90-el);
MagE = efield';
surf(MagE)

%%
load('testX.mat');
%polx=circshift(y,16);
polx=y;
load('testY.mat');
poly=circshift(y,16);
%poly=y;
aux=circshift(polx,16);
for j=1:16
    R(16,j)=poly(2*j);
end

for j=1:1:32
    R(j,8)=aux(j);
end
% for j=1:16
%     R(1,j)=poly(33-j);
% end
NUM_HALF=16;
surf(R);
th=180:-180/15:0;
ph=-180:360/31:180;
ph=ph';
%%
for i = 1:1:16
    for j=1:1:32
            R(j,i)=(R(16,i).*(1-abs(j-16)/16))/2+(R(j,8).*(1-abs(i-8)/8))/2;
    end
end
R(32,16)=R(16,16).*0.0312/2+R(32,8).*0.0625/2;
surf(R);
th=180:-180/15:0;
ph=-180:360/31:180;
ph=ph';
%patternCustom(R,th,ph);