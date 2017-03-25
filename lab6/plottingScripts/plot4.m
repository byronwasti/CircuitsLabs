clear;

nmos4 = csvread('../data/experiment1_transistor4_1.csv', 1);

[Is, VT, kappa] = ekvfit(nmos4(85:1000,1), nmos4(85:1000,2), 1e-3, 'on')

%  Is    = 
%  VT    = 
%  kappa = 