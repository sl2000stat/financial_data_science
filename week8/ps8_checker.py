################################################
##                                            ##
##   Problem Set Week 8                       ##
##                                            ##
################################################

# Note: Enter your results as actual numbers. We check your solution by allowing some minor margin of error. (No need to round your answers!)


########### Task (2) ###########

########### Task (2.1) ###########
# ols estimate of AR(1) coef
coeff_const_AI_PA = 0.0089
coeff_rlag1_AI_PA = -0.0941
# t-stat for AR(1) coef
t_stat_const_AI_PA = 2.9631
t_stat_rlag1_AI_PA = -1.5117
# variance of r. Hint: var(y) = sum (r-mean(r)/(len(r)-1)
var_r_AI_PA = 0.002265325484789007
# variance of eps Hint: var(eps) = eps.T eps / (len(r)-1-1)
var_eps_AI_PA = 0.002253921710688763
# variance of mu. Hint: var(mu) = sum(mu-mean(mu)/(len(mu)-1)
var_mu_AI_PA = 0.000020277

########### Task (2.2) ###########

ticker = "MUV2.DE"
t_stat_const_ticker = 0.5921
t_stat_rlag1_ticker = -2.5438
adj_rsqr_ticker = 0.021085079446328536


########### Task (3) ###########

# ols estimate of AR(1) coef
coeff_const_market = 0.0046
coeff_rlag1_market = 0.0398
# t-stat for AR(1) coef
t_stat_const_market = 1.3432
t_stat_rlag1_market = 0.6345
# adj_R^2
adj_rsqr_market = -0.0024
# variance of r. Hint: var(y) = sum (r-mean(r)/(len(r)-1)
var_r_market = 0.0030133318157624794
# variance of eps Hint: var(eps) = eps.T eps / (len(r)-1-1)
var_eps_market = 0.0030204365557556464
# variance of mu. Hint: var(mu) = sum(mu-mean(mu)/(len(mu)-1)
var_mu_market = 0.00000478674
