# Tackling heavy tailed heteroscedastic noise in linear regression 

Gaussian linear models are often insufficient in practical applications, where noise can be heavy tailed. In this problem, we consider a simple linear model with an added independent noise from a distribution that depends on predictors as well as on global parameters; however, the noise distribution has conditional mean zero given the predictor. The goal is to derive a good estimator for the parameters of the linear regression based on a sample of observed data.

We approach this problem using 3 distinct approaches. First approach is to tackle heavy tails using robust regression (Huber and Tukey’s bi-weight penalty); second approach is using a weighted least squares (WLS) method to tackle non constant variance and the third approach is to use a maximum likelihood formulation (MLE) to tackle both non constant variance and heavy tails using a parametric form for variance.

Data sets
---------
*data_1_1.csv, data_1_2.csv, data_1_3.csv, data_1_4.csv, data_1_5.csv*

Python scripts
--------
*Aggregate_data.py*; Loads aggregated data.  Plots residuals of OLS fits which is used as a diagnostic and saves the resultant plots in to a .pdf file.

*globals.py*; 
Defines an object to store coefficients of our regression; also defines an object to store average test errors.

*irls.py*; Runs a robust regression with Huber and Tukey penalty and returns the regression coefficients. 

*k_fold_cross_validation.py*; Performs k fold cross validation across every data set and for every method outlined. Saves the average test errors on to a nested dictionary.

*Load_data.py*; Loads data sets in to a dictionary.

*main.py*; Main file. 

*MLE.py*; Runs a maximum likelihood regression with heteroskedastic double exponential noise.

*wls.py*; Runs a weighted linear regression with iterative refinement of variance.

Run main.py for point estimates. Run k_fold_cross_validation.py for cross validation. Note that both of these create new .csv files and to ensure that they run correctly, please make sure that the only .csv files in the working directory are the data set .csv files.

Output files
-------------
*regression_estimates.csv*; A .csv file which contains the point estimates of linear regression fits.

*avg_test_error.csv*; A .csv file which contains the average mean squared test error for all data sets across different linear regression methods that have been used.

Plots:
--------
linear_fits.pdf, ols_fits.pdf, residuals_QQplot.pdf, residuals_scatterplot.pdf, squared_residuals_scatterplot.pdf

Project Report: 
----------------
Report.pdf; A write up with summary and explanations of the methods used. 
