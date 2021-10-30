################################################
##                                            ##
##   Problem Set Week 5                       ##
##                                            ##
################################################

# Note: Please round all numeric answers to two decimals.
# Use 252 trading days for annualization if required

# Write a class called "CAPM". The members of the class are: 
# alpha, beta, t-stat of alpha, t-stat of beta, adjusted R^2. 
# The class method "fit_SML()" uses the GLS package of 
# the statsmodels to fit the CAPM SML and to pin down alpha,
# beta, t-stat of alpha, t-stat of beta, adjusted R^2. 
# Also, store the regression package's summary table as a 
# private member of the CAPM class. Let class method 
# "display_Regression_Table()" print out the regression 
# summary table.

# !!! IMPORTANT !!!
# - Please round all numeric answers to two decimals. 
#   That is, DON'T report your results in percentage terms.
# - Use 252 trading days for annualization if required
# - In order to answer the questions below for the Praktomat, estimate your 
#   CAPM class by using the provided files apple.csv, sp500.csv and riskfree.csv.

# Data preparation:
# Load the provided files apple.csv, sp500.csv and riskfree.csv.
# Compute excess log returns for apple and sp500 based on the Close prices
# relative to the provided risk-free rate. The risk-free rate is
# given in annualized terms (252 trading days). It needs to be transformed
# into a daily risk-free rate first.
# Use your CAPM class and the provided files to perform the calculations 
# and to answer the questions below. Therefore, use the S&P 500 data as a proxy
# for the market return and compute the CAPM parameters for the Apple stock.

########### Task (i) ###########

# Estimate the capm alpha, beta and the corresponding t-stats for these parameters as well as the adjusted R^2 for Apple
# Insert the actual numbers and round to two decimals
capm_alpha = 0.00
capm_beta = 1.05
capm_alpha_t_stat = 4.27
capm_beta_t_stat = 49.61
capm_r_squared_adjusted = 0.37

# Did the asset earn a meaningful positive alpha?
# Insert a string 'yes' or 'no'
answer_alpha = 'no'

# Are the coefficients significant?
# Insert a string 'yes' or 'no'
answer_coefficients = 'yes'

########### Task (ii) ###########

# Compute Apple's annualized total risk, idiosyncratic risk and systematic risk.
# Insert the actual numbers and round to two decimals
total_risk_annualized = 5.37
idiosyncratic_risk_annualized = 4.28
systematic_risk_annualized = 3.25

# How much of the asset's risk (fraction of total risk) is diversifiable and how much is systematatic?
# Insert the actual numbers and round to two decimals
diversifiable_risk = 0.8
non_diversifiable_risk = 0.61

########### Task (iii) ###########

# Compare the annualized average excess log return with the annualized SML-implied expected return.
# Insert the actual numbers and round to two decimals
avg_excess_return = 0.34
sml_expected_return = 0.06

# How large has been the annualized Sharpe Ratio for Apple?
# Use the asset's mean excess return for the calculation.
# Insert the actual numbers and round to two decimals
sr_annualized = 0.06