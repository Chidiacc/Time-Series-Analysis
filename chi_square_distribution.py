# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:49:16 2015

@author: chidiac
"""

import numpy as np
import math
import os 

route='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_File/'
route2= '/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/'

#GHz=[2.6, 23, 32]
#X=np.arange (1.0, 3.2, 0.2) 
#Z=np.arange(0,1.2, 0.005 ) 
#for u in GHz: 
#    name='PSD_'+('{}'.format(u))+'_inter.dat'
#    for y in range (X.shape[0]):
#        z=X[y]
#        for Y in range (Z.shape[0]):
#            w=Z[Y]
#            print z 
#            route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'+('{}'.format(u))+'_PSD_sim/'+('{}'.format(u))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#            H=[]
#            route_mean='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/mean_'+('{}'.format(u))+'GHz_'+('{}'.format(z))+'/'
#            route_quantile='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/quantile_'+('{}'.format(u))+'GHz_'+('{}'.format(z))+'/'
#            if not os.path.isdir(route_mean):
#                os.makedirs(route_mean)
#            if not os.path.isdir(route_quantile):
#                os.makedirs(route_quantile)
#            PSD_obs=np.loadtxt(route+name) 
#            result=[]
#            result1=[]
#            for i in range (PSD_obs.shape[0]):
#                for o in range (1,100):
#                    name1='PSD_'+('{}'.format(u))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#                    Data=np.loadtxt(route1+name1)  
#                    D=Data[i,2]
#                    H.append(D)
#                G=np.array(H)
#                e=PSD_obs[i,1]
#                C=np.mean(G)
#                n=len(G)
#                Q=np.percentile(G,95)
#                Delta=np.sqrt((np.mean(np.square(G)))/n)
#                result.append([e,C,Delta])
#                result1.append([e,Q])
#            name_mean='mean_'+('{}'.format(u))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat' 
#            name_quantile='quantile_'+('{}'.format(u))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat'
#            mean=np.array(result)
#            quantile=np.array(result1)
#            np.savetxt(route_mean+name_mean, mean)
#            np.savetxt(route_quantile+name_quantile, quantile)
        
#for u in GHz:
#    name='PSD_'+('{}'.format(u))+'_inter.dat'
#    PSD_obs= np.loadtxt(route+name)
#    for y in range (X.shape[0]):
#        z=X[y]
#        Chi=[]
#        route_mean='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/mean_'+('{}'.format(u))+'GHz_'+('{}'.format(z))+'/'
#        for Y in range (Z.shape[0]):
#            w=Z[Y]
#            name_mean='mean_'+('{}'.format(u))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat'       
#            mean=np.loadtxt(route_mean+name_mean)
#            S=0
#            for i in range (PSD_obs.shape[0]):
#                A=((mean[i,1]-PSD_obs[i,2])**2)/((mean[i,2])**2)
#                S=S+A
#            Chi.append([w,S])
#        Chi=np.array(Chi)
#        name2='Chi_Square_'+('{}'.format(u))+'_'+('{}'.format(z))+'.dat' 
#        np.savetxt(route2+name2 , Chi)

       
X=np.arange (1.0, 3.2, 0.2) 
Z=np.arange(0,1.2, 0.005 )  
name='PSD_Rflx_inter.dat'
for y in range (X.shape[0]):
    z=X[y]
    for Y in range (Z.shape[0]):
        w=Z[Y]
        print z 
        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/Rflx_PSD_sim/Rflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
        H=[]
        route_mean='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/mean_Rflx_'+('{}'.format(z))+'/'
        route_quantile='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/quantile_Rflx_'+('{}'.format(z))+'/'
        if not os.path.isdir(route_mean):
            os.makedirs(route_mean)
        if not os.path.isdir(route_quantile):
            os.makedirs(route_quantile)
        PSD_obs=np.loadtxt(route+name) 
        result=[]
        result1=[]
        for i in range (PSD_obs.shape[0]):
            for o in range (1,101):
                name1='PSD_Rflxsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
                Data=np.loadtxt(route1+name1)  
                D=Data[i,2]
                H.append(D)
            G=np.array(H)
            e=PSD_obs[i,1]
            C=np.mean(G)
            n=len(G)
            Q=np.percentile(G,95)
            Delta=np.sqrt((np.mean(np.square(G)))/n)
            result.append([e,C,Delta])
            result1.append([e,Q])
        name_mean='mean_Rflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat' 
        name_quantile='quantile_Rflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat'
        mean=np.array(result)
        quantile=np.array(result1)
        np.savetxt(route_mean+name_mean, mean)
        np.savetxt(route_quantile+name_quantile, quantile)
        
name='PSD_Rflx.dat'
PSD_obs= np.loadtxt(route+name)
for y in range (X.shape[0]):
    z=X[y]
    Chi=[]
    route_mean='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/mean_Rflx_'+('{}'.format(z))+'/'
    for Y in range (Z.shape[0]):
        w=Z[Y]
        name_mean='mean_Rflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat'       
        mean=np.loadtxt(route_mean+name_mean)
        S=0
        for i in range (PSD_obs.shape[0]):
            A=((mean[i,1]-PSD_obs[i,2])**2)/((mean[i,2])**2)
            S=S+A
        Chi.append([w,S])
    Chi=np.array(Chi)
    name2='Chi_Square_Rflx_'+('{}'.format(z))+'.dat' 
    np.savetxt(route2+name2 , Chi)  
#    
#X=np.arange (1.0, 3.2, 0.2) 
#Z=np.arange(0,1.2, 0.005 )  
#name='PSD_Vflx_inter.dat'
#for y in range (X.shape[0]):
#    z=X[y]
#    for Y in range (Z.shape[0]):
#        w=Z[Y]
#        print z 
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/Vflx_PSD_sim/Vflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        H=[]
#        route_mean='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/mean_Vflx_'+('{}'.format(z))+'/'
#        route_quantile='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/quantile_Vflx_'+('{}'.format(z))+'/'
#        if not os.path.isdir(route_mean):
#            os.makedirs(route_mean)
#        if not os.path.isdir(route_quantile):
#            os.makedirs(route_quantile)
#        PSD_obs=np.loadtxt(route+name) 
#        result=[]
#        result1=[]
#        for i in range (PSD_obs.shape[0]):
#            for o in range (1,101):
#                name1='PSD_Vflxsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#                Data=np.loadtxt(route1+name1)  
#                D=Data[i,2]
#                H.append(D)
#            G=np.array(H)
#            e=PSD_obs[i,1]
#            C=np.mean(G)
#            n=len(G)
#            Q=np.percentile(G,95)
#            Delta=np.sqrt((np.mean(np.square(G)))/n)
#            result.append([e,C,Delta])
#            result1.append([e,Q])
#        name_mean='mean_Vflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat' 
#        name_quantile='quantile_Vflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat'
#        mean=np.array(result)
#        quantile=np.array(result1)
#        np.savetxt(route_mean+name_mean, mean)
#        np.savetxt(route_quantile+name_quantile, quantile)
#        
#name='PSD_Vflx_inter.dat'
#PSD_obs= np.loadtxt(route+name)
#for y in range (X.shape[0]):
#    z=X[y]
#    Chi=[]
#    route_mean='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/mean_Vflx_'+('{}'.format(z))+'/'
#    for Y in range (Z.shape[0]):
#        w=Z[Y]
#        name_mean='mean_Vflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat'       
#        mean=np.loadtxt(route_mean+name_mean)
#        S=0
#        for i in range (PSD_obs.shape[0]):
#            A=((mean[i,1]-PSD_obs[i,2])**2)/((mean[i,2])**2)
#            S=S+A
#        Chi.append([w,S])
#    Chi=np.array(Chi)
#    name2='Chi_Square_Vflx_'+('{}'.format(z))+'.dat' 
#    np.savetxt(route2+name2 , Chi)
#    
    
#X=np.arange (1.0, 3.2, 0.2) 
#Z=np.arange(0,1.2, 0.005 )  
#name='PSD_Jflx_inter.dat'
#for y in range (X.shape[0]):
#    z=X[y]
#    for Y in range (Z.shape[0]):
#        w=Z[Y]
#        print z 
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/Jflx_PSD_sim/Jflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        H=[]
#        route_mean='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/mean_Jflx_'+('{}'.format(z))+'/'
#        route_quantile='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/quantile_Jflx_'+('{}'.format(z))+'/'
#        if not os.path.isdir(route_mean):
#            os.makedirs(route_mean)
#        if not os.path.isdir(route_quantile):
#            os.makedirs(route_quantile)
#        PSD_obs=np.loadtxt(route+name) 
#        result=[]
#        result1=[]
#        for i in range (PSD_obs.shape[0]):
#            for o in range (1,101):
#                name1='PSD_Jflxsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#                Data=np.loadtxt(route1+name1)  
#                D=Data[i,2]
#                H.append(D)
#            G=np.array(H)
#            e=PSD_obs[i,1]
#            C=np.mean(G)
#            n=len(G)
#            Q=np.percentile(G,95)
#            Delta=np.sqrt((np.mean(np.square(G)))/n)
#            result.append([e,C,Delta])
#            result1.append([e,Q])
#        name_mean='mean_Jflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat' 
#        name_quantile='quantile_Jflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat'
#        mean=np.array(result)
#        quantile=np.array(result1)
#        np.savetxt(route_mean+name_mean, mean)
#        np.savetxt(route_quantile+name_quantile, quantile)
#        
#name='PSD_Jflx_inter.dat'
#PSD_obs= np.loadtxt(route+name)
#for y in range (X.shape[0]):
#    z=X[y]
#    Chi=[]
#    route_mean='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/mean_Jflx_'+('{}'.format(z))+'/'
#    for Y in range (Z.shape[0]):
#        w=Z[Y]
#        name_mean='mean_Jflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'.dat'       
#        mean=np.loadtxt(route_mean+name_mean)
#        S=0
#        for i in range (PSD_obs.shape[0]):
#            A=((mean[i,1]-PSD_obs[i,2])**2)/((mean[i,2])**2)
#            S=S+A
#        Chi.append([w,S])
#    Chi=np.array(Chi)
#    name2='Chi_Square_Jflx_'+('{}'.format(z))+'.dat' 
#    np.savetxt(route2+name2 , Chi)