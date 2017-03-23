pmos = csvread('../data/experiment1_pmos_1.csv', 1);

pmos_downsample = vertcat(pmos(120:200, :), downsample(pmos(201:1000, :), 8));

% make sure to set N > 10 to N > 3 on line 49 of linefit.m
[Is, VT, kappa] = ekvfit(pmos_downsample(:, 1), pmos_downsample(:, 2), 5e-3, 'on')

%  Is    = 5.9167e-09
%  VT    = -0.6725
%  kappa = -6.7837