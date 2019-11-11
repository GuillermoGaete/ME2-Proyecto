load('testX.mat');
polx=circshift(y,16);
load('testY.mat');
poly=circshift(y,16);

subplot(2,1,1);plot(theta);
subplot(2,1,2);plot(vertSlice);


