clear;
nmos = csvread('../data/experiment1_nmos_1.csv', 1);
nmos_downsample = vertcat(nmos(1:200, :), downsample(nmos(201:400, :), 4));

gm = diff(nmos_downsample(:,2)) ./ diff(nmos_downsample(:,1));
coeff1 = polyfit(log(nmos_downsample(32:60,2)), log(gm(32:60)), 1);
coeff2 = polyfit(log(nmos_downsample(62:250,2)), log(gm(61:249)), 1)

theoretical_gm1 = (exp(coeff1(1)) .* nmos_downsample(32:250,2)) ./ exp(coeff1(2) - 4.5);
theoretical_gm2 = (exp(coeff1(1)) .* sqrt(nmos_downsample(32:250,2))) ./ exp(coeff1(2) + 1.75);

% plot(nmos(:,1), nmos(:,2))
loglog(nmos_downsample(2:250,2), gm, '.')
hold on;
loglog(nmos_downsample(32:250,2), theoretical_gm1)
loglog(nmos_downsample(32:250,2), theoretical_gm2)

xlabel('I_{channel} (A)');
ylabel('g_m (mhos)');
legend('nMOS experimental data', '$g_m = \frac{\kappa}{U_T}I_{sat}$', '$g_m = \frac{\kappa}{U_T}\sqrt{I_s I_{sat}}$');
title('g_m vs. I_{channel}');
set(legend,'Interpreter','Latex');