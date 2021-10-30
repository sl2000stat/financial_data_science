################################################
##                                            ##
##   Problem Set Week 9                       ##
##                                            ##
################################################


########### Task G.3 ###########
# Hint
# with kappa_p_init : 0.014895, theta_p_init: 0.004660, kappa_q_init: 0.014895,
# theta_q_init: 0.004660, sigma_r_init:0.000378, sigma_y_init: 0.000777
# you will get the evaluation of llk is around -3646x.xxx

# Optimized parameters from L-BFGS-B
kappa_p_bfgs = 0.
theta_p_bfgs = 0.
kappa_q_bfgs = 0.
theta_q_bfgs = 0.
sigma_r_bfgs = 0.
sigma_y_bfgs = 0.

# Optimized parameters from dual_annealing
kappa_p_annealing = 0.
theta_p_annealing = 0.
kappa_q_annealing = 0.
theta_q_annealing = 0.
sigma_r_annealing = 0.
sigma_y_annealing = 0.

# ERP 120m
ERP_120m_0 = 0.
ERP_120m_10 = 0.
ERP_120m_100 = 0.
ERP_120m_500 = 0.

# As the task is to decompose bond returns, it is better to pair mu and eps.
# As eps can be computed only starting at second observations(1954-05-01),
# please also make mu starts at the second observations
mu_0 = 0.
mu_1 = 0.
mu_100 = 0.
mu_500 = 0.

eps_0 = 0.
eps_1 = 0.
eps_100 = 0.
eps_500 = 0.
