clear;

nmos3 = csvread('../data/experiment1_transistor3_4.csv', 1);

[Is, VT, kappa] = ekvfit(nmos3(100:1000,1), nmos3(100:1000,2), 1e-3, 'on')

%  Is    = 
%  VT    = 
%  kappa = 