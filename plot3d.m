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
% if max(polx)>max(poly)
%     poly=poly+(max(polx)-max(poly))
% else
%     polx=polx+(max(poly)-max(polx))
% end
if poly(16)>aux(16)
    aux=aux+ploy(16)-aux(16);
else
    poly=poly-poly(16)+aux(16);
end
poly=interp1(1:length(poly),poly,linspace(1,length(poly),361),'Linear Interpolation');
aux=interp1(1:length(aux),aux,linspace(1,length(aux),361),'Linear Interpolation');
for j=1:180
    R(181,j)=poly(2*j);
end
R(181,181)=poly(361);
for j=1:1:361
    R(j,91)=aux(j);
end


% for j=1:16
%     R(1,j)=poly(33-j);
% end
NUM_HALF=16;
surf(R);
th=180:-180:0;
ph=-180:360:180;
ph=ph';
%%
for i = 1:1:181
    for j=1:1:361
            R(j,i)=(R(181,i).*(1-abs(j-181)/181))/2+(R(j,91).*(1-abs(i-91)/91))/2;
    end
end
R(361,181)=R(181,181).*0.0312/2+R(361,91).*0.0625/2;
surf(R);
th=180:-1:0;
ph=-180:1:180;
ph=ph';
patternCustom(R,th,ph);