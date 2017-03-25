clear;

nmos1 = csvread('../data/experiment1_transistor1_3.csv', 1);

[Is, VT, kappa] = ekvfit(nmos1(80:1000,1), nmos1(80:1000,2), 1e-3, 'on')

%  Is    = 
%  VT    = 
%  kappa = 