# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:42:01 2015

@author: chidiac
"""


#var_x = var(data$V2)
#frac_var = sqrt((var_x - err_sq_mean)/(mean_x*mean_x))
#fac_A = sqrt(1/(2*N))*(err_sq_mean/(mean_x*mean_x*frac_var))
#fac_B = sqrt(err_sq_mean/N)*(1/(mean_x))
#err_frac_var = sqrt(fac_A*fac_A + fac_B*fac_B)
#cat(frac_var, err_frac_var)

import numpy as np


#GHz=[2.6, 5, 8, 10, 15, 23, 32, 42, 86, 142, 230, 350]
#for u in GHz:
#    
#    
#    route = "/media/celine/My Passport/DOCUMENTS/Masterarbeit/Used_Data/"
#    name=('{}'.format(u))+'GHz.dat'
#    
#    data=np.loadtxt(route+name)
#    N=len(data)
#    mean=data[:,1].mean()
#    err_sq_mean=((data[:,2])**2).mean()
#    var=data[:,1].var()
#    frac_var=np.sqrt((var-err_sq_mean)/(mean**2))
#    frac_A = np.sqrt(1/(2*N))*(err_sq_mean/(frac_var*(mean**2)))
#    frac_B= np.sqrt(err_sq_mean/N)*(1/mean)
#    err_frac_var=np.sqrt(frac_A**2 + frac_B**2)
#    
#    print "**********************************************************"
#    print "Frequency:{}".format(u)
#    print "Fractional Variability:" , frac_var
#    print "Error on Fractional Variability:" , err_frac_var
#    print "**********************************************************"
                    

    
    
route = "/media/celine/My Passport/DOCUMENTS/Masterarbeit/Used_Data/"
name='gammamonthly.dat'
data=np.loadtxt(route+name)
N=len(data)
mean=data[:,1].mean()
err_sq_mean=((data[:,2])**2).mean()
var=data[:,1].var()
frac_var=np.sqrt((var-err_sq_mean)/(mean**2))
frac_A = np.sqrt(1/(2*N))*(err_sq_mean/(frac_var*(mean**2)))
frac_B= np.sqrt(err_sq_mean/N)*(1/mean)
err_frac_var=np.sqrt(frac_A**2 + frac_B**2)
print "**********************************************************"
print "Gamma Monthly"
print "Fractional Variability:" , frac_var
print "Error on Fractional Variability:" , err_frac_var
print "**********************************************************"    