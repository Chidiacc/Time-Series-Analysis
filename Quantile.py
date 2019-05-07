# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:44:58 2015

@author: celine
"""

"""
File    quantile.py
Desc    computes sample quantiles 
Author  Ernesto P. Adorio, PhD.
        UPDEPP (U.P. at Clarkfield)
Version 0.0.1 August 7. 2009
"""
import numpy as np
import math as m
 

route='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/DCF/HardXrayvs230GHz/'
bin=20
l=np.arange(-700,701,bin)
L=[]
for k in range (l.shape[0]):
   W=l[k]-bin/2
   L.append(W)
L=np.array(L)
print L
result=[]
H=[]
q=5
for n in range (L.shape[0]):
    for i in range (1,2001):
        name='DCF_HardXray'+('{}'.format(i))+'vs230GHz_'+('{}'.format(bin))+'_fulldata.dat'
        Data=np.loadtxt(route+name)  
        X=Data[n,1]
        H.append(X)
    G=np.array(H)
    e=L[n]
    C=np.percentile(G, q)
    result.append([e,C])
route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/Quantile/'
name2='Quantile_HardXrayvs230GHz_5_fulldata_20.dat' 
Q=np.array(result)
np.savetxt(route1+name2 , Q)
    
    
    
    
#route='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/DCF/HardXrayvs230GHz/'
#bin=20
#l=np.arange(-700,701,bin)
#L=[]
#for k in range (l.shape[0]):
#   W=l[k]-bin/2
#   L.append(W)
#L=np.array(L)
#print L
#result=[]
#H=[]
#q=95
#for n in range (L.shape[0]):
#    for i in range (1,2001):
#        name='DCF_HardXray'+('{}'.format(i))+'vs230GHz_'+('{}'.format(bin))+'_fulldata.dat'
#        Data=np.loadtxt(route+name)  
#        X=Data[n,1]
#        H.append(X)
#    G=np.array(H)
#    e=L[n]
#    C=np.percentile(G, q)
#    result.append([e,C])
#route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/Quantile/'
#name2='Quantile_HardXrayvs230GHz_95_fulldata_20.dat' 
#Q=np.array(result)
#np.savetxt(route1+name2 , Q)
       
#route='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/DCF/Soft-Xray2to10KeVvs230GHz/'
#bin=20
#l=np.arange(-700,701,bin)
#L=[]
#for k in range (l.shape[0]):
#   W=l[k]-bin/2
#   L.append(W)
#L=np.array(L)
#print L
#result=[]
#H=[]
#q=5
#for n in range (L.shape[0]):
#    for i in range (1,2001):
#        name='DCF_Soft-Xray2to10KeV'+('{}'.format(i))+'vs230GHz_'+('{}'.format(bin))+'_fulldata.dat'
#        Data=np.loadtxt(route+name)  
#        X=Data[n,1]
#        H.append(X)
#    G=np.array(H)
#    e=L[n]
#    C=np.percentile(G, q)
#    result.append([e,C])
#route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/Quantile/'
#name2='Quantile_Soft-Xray2to10KeVvs230GHz_5_fulldata_20.dat' 
#Q=np.array(result)
#np.savetxt(route1+name2 , Q)
#
#
#route='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/DCF/Soft-Xray2to10KeVvs230GHz/'
#bin=20
#l=np.arange(-700,701,bin)
#L=[]
#for k in range (l.shape[0]):
#   W=l[k]-bin/2
#   L.append(W)
#L=np.array(L)
#print L
#result=[]
#H=[]
#q=95
#for n in range (L.shape[0]):
#    for i in range (1,2001):
#        name='DCF_Soft-Xray2to10KeV'+('{}'.format(i))+'vs230GHz_'+('{}'.format(bin))+'_fulldata.dat'
#        Data=np.loadtxt(route+name)  
#        X=Data[n,1]
#        H.append(X)
#    G=np.array(H)
#    e=L[n]
#    C=np.percentile(G, q)
#    result.append([e,C])
#route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/Quantile/'
#name2='Quantile_Soft-Xray2to10KeVvs230GHz_95_fulldata_20.dat' 
#Q=np.array(result)
#np.savetxt(route1+name2 , Q)    
#
#
#route='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/DCF/Soft-Xray10to50KeVvs230GHz/'
#bin=30
#l=np.arange(-700,701,bin)
#L=[]
#for k in range (l.shape[0]):
#   W=l[k]-bin/2
#   L.append(W)
#L=np.array(L)
#print L
#result=[]
#H=[]
#q=5
#for n in range (L.shape[0]):
#    for i in range (1,2001):
#        name='DCF_Soft-Xray10to50KeV'+('{}'.format(i))+'vs230GHz_'+('{}'.format(bin))+'_fulldata.dat'
#        Data=np.loadtxt(route+name)  
#        X=Data[n,1]
#        H.append(X)
#    G=np.array(H)
#    e=L[n]
#    C=np.percentile(G, q)
#    result.append([e,C])
#route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/Quantile/'
#name2='Quantile_Soft-Xray10to50KeVvs230GHz_5_fulldata_20.dat' 
#Q=np.array(result)
#np.savetxt(route1+name2 , Q)    
#
#
#route='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/DCF/Soft-Xray10to50KeVvs230GHz/'
#bin=30
#l=np.arange(-700,701,bin)
#L=[]
#for k in range (l.shape[0]):
#   W=l[k]-bin/2
#   L.append(W)
#L=np.array(L)
#print L
#result=[]
#H=[]
#q=95
#for n in range (L.shape[0]):
#    for i in range (1,2001):
#        name='DCF_Soft-Xray10to50KeV'+('{}'.format(i))+'vs230GHz_'+('{}'.format(bin))+'_fulldata.dat'
#        Data=np.loadtxt(route+name)  
#        X=Data[n,1]
#        H.append(X)
#    G=np.array(H)
#    e=L[n]
#    C=np.percentile(G, q)
#    result.append([e,C])
#route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Lightcurves_simulation/Quantile/'
#name2='Quantile_Soft-Xray10to50KeVvs230GHz_95_fulldata_30.dat' 
#Q=np.array(result)
#np.savetxt(route1+name2 , Q)   


