clear;

nmos2 = csvread('../data/experiment1_transistor2_4.csv', 1);

[Is, VT, kappa] = ekvfit(nmos2(1:930,1), nmos2(1:930,2), 1e-3, 'on')

%  Is    = 
%  VT    = 
%  kappa = 