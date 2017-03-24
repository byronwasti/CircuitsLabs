clear;
pmos = csvread('../data/experiment1_pmos_1.csv', 1);
pmos_downsample = vertcat(downsample(pmos(1:100, :),5), pmos(101:600, :), downsample(pmos(601:1000, :),10));

gm = (-1 .* diff(pmos_downsample(:,2))) ./ diff(pmos_downsample(:,1));

coeff1 = polyfit(log(pmos_downsample(55:300,2)), log(gm(55:300)), 1)
coeff2 = polyfit(log(pmos_downsample(302:560,2)), log(gm(301:559)), 1)

theoretical_gm1 = (exp(coeff1(1)) .* pmos_downsample(1:560,2)) ./ exp(coeff1(2));
theoretical_gm2 = (exp(coeff1(1)) .* sqrt(pmos_downsample(1:560,2))) ./ exp(coeff1(2) + 7);

% plot(pmos(:,1), pmos(:,2))
loglog(pmos_downsample(2:560,2), gm, '.')
hold on;
loglog(pmos_downsample(1:560,2), theoretical_gm1)
loglog(pmos_downsample(1:560,2), theoretical_gm2)

xlabel('I_{channel} (A)');
ylabel('g_m (mhos)');
legend('pMOS experimental data', '$g_m = \frac{\kappa}{U_T}I_{sat}$', '$g_m = \frac{\kappa}{U_T}\sqrt{I_s I_{sat}}$');
title('g_m vs. I_{channel}');
set(legend,'Interpreter','Latex');