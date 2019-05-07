# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:35:17 2015

@author: chidiac
"""
import numpy as np
from DELCgen import *
import os

#------- Input parameters -------

u=350
# File Route
route = "/media/My Passport/DOCUMENTS/Masterarbeit/Used_Data/"
datfile = ('{}'.format(u))+'GHz.dat' 

X= np.arange(1,5.2, 0.2)
Z=np.arange(0,5.02, 0.02)
for y in range (X.shape[0]):
    z=X[y]
    for Y in range (Z.shape[0]):
        w=Z[Y]
        route1= r'/media/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u))+'GHz/'+('{}'.format(u))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
        if not os.path.isdir(route1):
            os.makedirs(route1)
        A= w
        v_bend= 5.66
        a_low=X[y]
        a_high = X[y]
        c=0
        # Probability density function params
        kappa,theta,lnmu,lnsig,weight = 19.29, 1.17, 1.29, 43.3, 292.399
        # Simulation params
        RedNoiseL,RandomSeed,aliasTbin, tbin = 100,12,1,8 
        
        #--------- Commands ---------------
        
        # load data lightcurve
        datalc = Load_Lightcurve(route+datfile,tbin)
        
        # create mixture distribution to fit to PDF
        mix_model = Mixture_Dist([st.gamma,st.lognorm],[3,3],[[[2],[0]],[[2],[0],]])
        
        
        # estimate underlying variance of data light curve
        datalc.STD_Estimate()
        
        # simulate artificial light curve with Timmer & Koenig method
        tklc = Simulate_TK_Lightcurve(datalc,BendingPL, (A,v_bend,a_low,a_high,c),
                                      RedNoiseL,aliasTbin,RandomSeed)
                                      
        # simulate artificial light curve with Emmanoulopoulos method, scipy distribution
        delc_mod = Simulate_DE_Lightcurve(datalc,BendingPL, (A,v_bend,a_low,a_high,c),
                                          mix_model, (kappa, theta, lnsig, np.exp(lnmu),
                                                                      weight,1-weight))
        
        # simulate artificial light curve with Emmanoulopoulos method, using the PSD
        # and PDF of the data light curve, with default parameters (bending power law
        # for PSD and mixture distribution of gamma and lognormal distribution for PDF)
        delc = datalc.Simulate_DE_Lightcurve()
        
        # save the simulated light curve as a txt file
        delc.Save_Lightcurve('lightcurve.dat')
        for j in range(1, 201):
            delc = datalc.Simulate_DE_Lightcurve()
            Data=np.array([delc.time, delc.flux])
            name=('{}'.format(u))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(j))+'.dat'
            np.savetxt(route1+name , Data.T)