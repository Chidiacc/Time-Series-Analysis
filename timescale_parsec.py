# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:43:31 2015

@author: chidiac
"""
#References: 
#beta_app = 15 c (Lister et al. 2013 AJ,146,120)
#viewing angle between 5 and 11 degree (Liu & Shen 2009, RAA, 9, 5)

import numpy as np
import math as m

#speed of light in pc/day
c=0.000839428867
beta=7*c
#theta_1=(5*m.pi)/180
theta_2=(9.8*m.pi)/180
#theta_3=(11*m.pi)/180

time_lag=120
error_time_lag=10

#dist_1=(beta*time_lag)/(m.sin(theta_1))
dist_2=(beta*time_lag)/(m.sin(theta_2))
#dist_3=(beta*time_lag)/(m.sin(theta_3))

#err_dist_1=(beta*error_time_lag)/(m.sin(theta_1))
err_dist_2=(beta*error_time_lag)/(m.sin(theta_2))
#err_dist_3=(beta*error_time_lag)/(m.sin(theta_3))

#print "dist_1=", dist_1
print "dist_2=", dist_2
#print "dist_3=", dist_3
#print "err_dist_1=", err_dist_1
print "err_dist_2=", err_dist_2
#print "err_dist_3=", err_dist_3


tvar=14.5
c=0.000839428867
beta=7
z=0.158

R=(c*tvar*beta)/(1+z)
print "R=" , R


##############################################################################
# From schwarzschild radius to pc
#for 3C 273
M=(6.6)*10**9
R_S=3*M  # Schwarzschild radius in km
R_s_pc= R_S*(3.24e-14) # Schwarzschild radius in pc

# Size of the corona is between 20-30 Rs
R1=20*R_s_pc
R2=30*R_s_pc

print "R1= ", R1
print "R2= ", R2
