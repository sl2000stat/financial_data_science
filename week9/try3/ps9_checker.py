################################################
##                                            ##
##   Problem Set Week 9                       ##
##                                            ##
################################################


########### Task G.3 ###########

# Optimized parameters from L-BFGS-B
kappa_p_bfgs = 0.014895
theta_p_bfgs = 0.00466
kappa_q_bfgs = 0.014895
theta_q_bfgs = 0.00466
sigma_r_bfgs = 0.00037794
sigma_y_bfgs = 0.000777

# Optimized parameters from dual_annealing
kappa_p_annealing = 0.014917206718773097
theta_p_annealing = 0.004701016867372424
kappa_q_annealing = 0.00264551787458
theta_q_annealing = 0.01561250660119
sigma_r_annealing = 0.000398165763
sigma_y_annealing = 0.000770098450

# ERP 120m
ERP_120m_0 = -0.00257363258
ERP_120m_10 = -0.00197166197
ERP_120m_100 = -0.000235208314
ERP_120m_500 = 0.00233474310

# As the task is to decompose bond returns, it is better to pair mu and eps.
# As eps can be computed only starting at second observations(1954-05-01),
# please also make mu starts at the second observations
mu_0 = -0.0019402992481888856
mu_1 = -0.0021792155412908567
mu_100 = 0.0026263
mu_500 = 0.0063050

eps_0 = 0.0216966
eps_1 = 0.0149258
eps_100 = 0.0063152
eps_500 = 0.011430777
