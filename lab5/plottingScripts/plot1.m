nmos = csvread('../data/experiment1_nmos_1.csv', 1);

[Is, VT, kappa] = ekvfit(nmos(:,1), nmos(:,2), 1e-3, 'on')

%  Is    = 1.9361e-06
%  VT    = 0.5576
%  kappa = 0.6821