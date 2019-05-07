# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:02:02 2015

@author: chidiac
"""
import numpy as np
import math
import os
#import the data files

X=np.arange (2.0, 3.2, 0.2) 
Z=np.arange(0.46,1.2, 0.005 ) 
for y in range (X.shape[0]): 
    z=X[y] 
    print z
    for Y in range (Z.shape[0]): 
        w=Z[Y] 
        print w
        route1= '/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/Soft-Xray2to10KeV/Soft-Xray2to10KeV_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/Rflx_PSD_sim/Soft-Xray2to10keV/Soft-Xray2to10KeV/Soft-Xray2to10KeV_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
        if not os.path.isdir(route1):
            os.makedirs(route1)
        if not os.path.isdir(route2):
            os.makedirs(route2)
        for u in range (1 , 21):
            name1 = 'Soft-Xray2to10KeVsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(u))+'.dat'

            Data1=np.loadtxt(route1+name1)
            #change the time(JD-JD(first term))
            A=Data1[0,0]
            dT=Data1[1,0]-A
            mean=Data1[:,1].mean()
            DATA=[]
            for l in range(Data1.shape[0]):
                T=Data1[l,0]-A
                F=Data1[l,1]-mean
                #e1=Data1[l,2]
                #e2=Data1[l,3]
                DATA.append([T,F])
            Data=np.array(DATA)
            #get the number of lines in the data file
            #N=sum(1 for row in Data)
            # or N=sum(1 for line in Data)
            #or simply write
            N=len(Data)
            #get the period of Data
            #generate an array for the j values
            L=np.arange(1, N/2, 1)
           #create an array with j and corresponding frequency in an array
            result =[]
            for k in range(L.shape[0]):
                j=L[k]
                f=j/(N*dT)
                result.append([j,f])
            D=np.array(result)    
            #calculate DFT using Euler's Formula to replace exp with sin and cos
            result1=[]
            for k in range(D.shape[0]):
                p=math.pi
                DFT2=0
                a=0
                b=0
                for i in range(Data.shape[0]):
                    J=D[k,0]
                    F=D[k,1]
                    t=Data[i,0]
                    x=Data[i,1]
                    c=2*p*F*t
                    ae=x*(math.cos(c))
                    be=x*(math.sin(c))
                    a=a+ae
                    b=b+be
                    DFT2=a**2 + b**2
                result1.append([J,F,DFT2])
            DFT=np.array(result1)
            #calculate the PSD value for each frequency
            result2=[]
            for l in range (DFT.shape[0]):
                PSD=math.log10((2*(DFT[l,2])*dT/N))
                Fj=math.log10((DFT[l,1]))
                result2.append([l,Fj,PSD])
            PSD=np.array(result2)
            name2='PSD_Soft-Xray20to10KeVsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(u))+'.dat'
            np.savetxt(route2+name2 , PSD)
            
            result3=[]
            n=len(PSD)
            bin=8
            l=np.arange(0,n,bin)
            print l
            k=len(l)-1
            true_psd=0
            mean_freq=0
            err_true_psd=0
            for j in range (l.shape[0]-1):
                m=l[j]+bin-1
                k=l[j]
                true_psd=PSD[k:m,2].mean()+0.20568
                mean_freq=PSD[k:m,1].mean()
                err_true_psd=0.31025/bin
                result3.append([mean_freq, true_psd, err_true_psd])
            fit=np.array(result3)
            print fit
            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
            print fit
            print (fit.shape)
            print slope
            name3= 'PSD_Soft-Xray20to10KeV_Fit_sim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(u))+'.dat'  
            np.savetxt(route2+name3 , fit)
#X=np.arange (1.0, 3.2, 0.2) 
#Z=np.arange(0,1.2, 0.005 ) 
#for y in range (X.shape[0]): 
#    z=X[y] 
#    print z
#    for Y in range (Z.shape[0]): 
#        w=Z[Y] 
#        print w
#        route1= '/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/Rflx/Rflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/Rflx_PSD_sim/Rflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        if not os.path.isdir(route1):
#            os.makedirs(route1)
#        if not os.path.isdir(route2):
#            os.makedirs(route2)
#        for u in range (1,101):
#            name1 = 'Rflxsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(u))+'.dat'
#
#            Data1=np.loadtxt(route1+name1)
#            #change the time(JD-JD(first term))
#            A=Data1[0,0]
#            dT=Data1[1,0]-A
#            mean=Data1[:,1].mean()
#            DATA=[]
#            for l in range(Data1.shape[0]):
#                T=Data1[l,0]-A
#                F=Data1[l,1]-mean
#                #e1=Data1[l,2]
#                #e2=Data1[l,3]
#                DATA.append([T,F])
#            Data=np.array(DATA)
#            #get the number of lines in the data file
#            #N=sum(1 for row in Data)
#            # or N=sum(1 for line in Data)
#            #or simply write
#            N=len(Data)
#            #get the period of Data
#            #generate an array for the j values
#            L=np.arange(1, N/2, 1)
#           #create an array with j and corresponding frequency in an array
#            result =[]
#            for k in range(L.shape[0]):
#                j=L[k]
#                f=j/(N*dT)
#                result.append([j,f])
#            D=np.array(result)    
#            #calculate DFT using Euler's Formula to replace exp with sin and cos
#            result1=[]
#            for k in range(D.shape[0]):
#                p=math.pi
#                DFT2=0
#                a=0
#                b=0
#                for i in range(Data.shape[0]):
#                    J=D[k,0]
#                    F=D[k,1]
#                    t=Data[i,0]
#                    x=Data[i,1]
#                    c=2*p*F*t
#                    ae=x*(math.cos(c))
#                    be=x*(math.sin(c))
#                    a=a+ae
#                    b=b+be
#                    DFT2=a**2 + b**2
#                result1.append([J,F,DFT2])
#            DFT=np.array(result1)
#            #calculate the PSD value for each frequency
#            result2=[]
#            for l in range (DFT.shape[0]):
#                PSD=math.log10((2*(DFT[l,2])*dT/N))
#                Fj=math.log10((DFT[l,1]))
#                result2.append([l,Fj,PSD])
#            PSD=np.array(result2)
#            name2='PSD_Rflxsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(u))+'.dat'
#            np.savetxt(route2+name2 , PSD)
#            
#            result3=[]
#            n=len(PSD)
#            bin=8
#            l=np.arange(0,n,bin)
#            print l
#            k=len(l)-1
#            true_psd=0
#            mean_freq=0
#            err_true_psd=0
#            for j in range (l.shape[0]-1):
#                m=l[j]+bin-1
#                k=l[j]
#                true_psd=PSD[k:m,2].mean()+0.20568
#                mean_freq=PSD[k:m,1].mean()
#                err_true_psd=0.31025/bin
#                result3.append([mean_freq, true_psd, err_true_psd])
#            fit=np.array(result3)
#            print fit
#            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
#            print fit
#            print (fit.shape)
#            print slope
#            name3= 'PSD_Rflx_Fit_sim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(u))+'.dat'  
#            np.savetxt(route2+name3 , fit)
#
#
#
#X=np.arange (1.0, 3.2, 0.2) 
#Z=np.arange(0,1.2, 0.005 ) 
#for y in range (X.shape[0]): 
#    z=X[y] 
#    print z
#    for Y in range (Z.shape[0]): 
#        w=Z[Y] 
#        print w
#        route1= '/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/Vflx/Vflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/Vflx_PSD_sim/Vflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        if not os.path.isdir(route1):
#            os.makedirs(route1)
#        if not os.path.isdir(route2):
#            os.makedirs(route2)
#        for u in range (1,101):
#            name1 = 'Vflxsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(u))+'.dat'
#
#            Data1=np.loadtxt(route1+name1)
#            #change the time(JD-JD(first term))
#            A=Data1[0,0]
#            dT=Data1[1,0]-A
#            mean=Data1[:,1].mean()
#            DATA=[]
#            for l in range(Data1.shape[0]):
#                T=Data1[l,0]-A
#                F=Data1[l,1]-mean
#                #e1=Data1[l,2]
#                #e2=Data1[l,3]
#                DATA.append([T,F])
#            Data=np.array(DATA)
#            #get the number of lines in the data file
#            #N=sum(1 for row in Data)
#            # or N=sum(1 for line in Data)
#            #or simply write
#            N=len(Data)
#            #get the period of Data
#            #generate an array for the j values
#            L=np.arange(1, N/2, 1)
#           #create an array with j and corresponding frequency in an array
#            result =[]
#            for k in range(L.shape[0]):
#                j=L[k]
#                f=j/(N*dT)
#                result.append([j,f])
#            D=np.array(result)    
#            #calculate DFT using Euler's Formula to replace exp with sin and cos
#            result1=[]
#            for k in range(D.shape[0]):
#                p=math.pi
#                DFT2=0
#                a=0
#                b=0
#                for i in range(Data.shape[0]):
#                    J=D[k,0]
#                    F=D[k,1]
#                    t=Data[i,0]
#                    x=Data[i,1]
#                    c=2*p*F*t
#                    ae=x*(math.cos(c))
#                    be=x*(math.sin(c))
#                    a=a+ae
#                    b=b+be
#                    DFT2=a**2 + b**2
#                result1.append([J,F,DFT2])
#            DFT=np.array(result1)
#            #calculate the PSD value for each frequency
#            result2=[]
#            for l in range (DFT.shape[0]):
#                PSD=math.log10((2*(DFT[l,2])*dT/N))
#                Fj=math.log10((DFT[l,1]))
#                result2.append([l,Fj,PSD])
#            PSD=np.array(result2)
#            name2='PSD_Vflxsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(u))+'.dat'
#            np.savetxt(route2+name2 , PSD)
#            
#            result3=[]
#            n=len(PSD)
#            bin=8
#            l=np.arange(0,n,bin)
#            print l
#            k=len(l)-1
#            true_psd=0
#            mean_freq=0
#            err_true_psd=0
#            for j in range (l.shape[0]-1):
#                m=l[j]+bin-1
#                k=l[j]
#                true_psd=PSD[k:m,2].mean()+0.20568
#                mean_freq=PSD[k:m,1].mean()
#                err_true_psd=0.31025/bin
#                result3.append([mean_freq, true_psd, err_true_psd])
#            fit=np.array(result3)
#            print fit
#            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
#            print fit
#            print (fit.shape)
#            print slope
#            name3= 'PSD_Vflx_Fit_sim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(u))+'.dat'  
#            np.savetxt(route2+name3 , fit)
#
#
#X=np.arange (1.0, 3.2, 0.2) 
#Z=np.arange(0,1.2, 0.005 ) 
#for y in range (X.shape[0]): 
#    z=X[y] 
#    print z
#    for Y in range (Z.shape[0]): 
#        w=Z[Y] 
#        print w
#        route1= '/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/Jflx/Jflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/Jflx_PSD_sim/Jflx_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        if not os.path.isdir(route1):
#            os.makedirs(route1)
#        if not os.path.isdir(route2):
#            os.makedirs(route2)
#        for u in range (1,101):
#            name1 = 'Jflxsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(u))+'.dat'
#
#            Data1=np.loadtxt(route1+name1)
#            #change the time(JD-JD(first term))
#            A=Data1[0,0]
#            dT=Data1[1,0]-A
#            mean=Data1[:,1].mean()
#            DATA=[]
#            for l in range(Data1.shape[0]):
#                T=Data1[l,0]-A
#                F=Data1[l,1]-mean
#                #e1=Data1[l,2]
#                #e2=Data1[l,3]
#                DATA.append([T,F])
#            Data=np.array(DATA)
#            #get the number of lines in the data file
#            #N=sum(1 for row in Data)
#            # or N=sum(1 for line in Data)
#            #or simply write
#            N=len(Data)
#            #get the period of Data
#            #generate an array for the j values
#            L=np.arange(1, N/2, 1)
#           #create an array with j and corresponding frequency in an array
#            result =[]
#            for k in range(L.shape[0]):
#                j=L[k]
#                f=j/(N*dT)
#                result.append([j,f])
#            D=np.array(result)    
#            #calculate DFT using Euler's Formula to replace exp with sin and cos
#            result1=[]
#            for k in range(D.shape[0]):
#                p=math.pi
#                DFT2=0
#                a=0
#                b=0
#                for i in range(Data.shape[0]):
#                    J=D[k,0]
#                    F=D[k,1]
#                    t=Data[i,0]
#                    x=Data[i,1]
#                    c=2*p*F*t
#                    ae=x*(math.cos(c))
#                    be=x*(math.sin(c))
#                    a=a+ae
#                    b=b+be
#                    DFT2=a**2 + b**2
#                result1.append([J,F,DFT2])
#            DFT=np.array(result1)
#            #calculate the PSD value for each frequency
#            result2=[]
#            for l in range (DFT.shape[0]):
#                PSD=math.log10((2*(DFT[l,2])*dT/N))
#                Fj=math.log10((DFT[l,1]))
#                result2.append([l,Fj,PSD])
#            PSD=np.array(result2)
#            name2='PSD_Jflxsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(u))+'.dat'
#            np.savetxt(route2+name2 , PSD)
#            
#            result3=[]
#            n=len(PSD)
#            bin=8
#            l=np.arange(0,n,bin)
#            print l
#            k=len(l)-1
#            true_psd=0
#            mean_freq=0
#            err_true_psd=0
#            for j in range (l.shape[0]-1):
#                m=l[j]+bin-1
#                k=l[j]
#                true_psd=PSD[k:m,2].mean()+0.20568
#                mean_freq=PSD[k:m,1].mean()
#                err_true_psd=0.31025/bin
#                result3.append([mean_freq, true_psd, err_true_psd])
#            fit=np.array(result3)
#            print fit
#            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
#            print fit
#            print (fit.shape)
#            print slope
#            name3= 'PSD_Jflx_Fit_sim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(u))+'.dat'  
#            np.savetxt(route2+name3 , fit)
##
#ua=2.6
#X=np.arange (1.0, 3.1, 0.2) 
#Z=np.arange(0,1.2, 0.005 )
#for y in range (X.shape[0]):
#    z=X[y]
#    for Y in range (Z.shape[0]):
#        w=Z[Y]
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(ua))+'GHz/'+('{}'.format(ua))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'
#        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'+('{}'.format(ua))+'_PSD_sim/'+('{}'.format(ua))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        #route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'
#        if not os.path.isdir(route1):
#            os.makedirs(route1)
#        if not os.path.isdir(route2):
#            os.makedirs(route2)
#        for o in range (1,100): 
#            name1= ('{}'.format(ua))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(o))+'.dat'
#            Data=np.loadtxt(route1+name1)
#            A=Data[0,0]
#            dT=Data[1,0]-A
#            #get the number of lines in the data file
#            #N=sum(1 for row in Data)
#            # or N=sum(1 for line in Data)
#            #or simply write
#            N=len(Data)
#            #get the period of Data
#            #generate an array for the j values
#            L=np.arange(1, N/2, 1)
#            #create an array with j and corresponding frequency in an array
#            result =[]
#            for m in range(L.shape[0]):
#                j=L[m]
#                f=j/(N*dT)
#                result.append([j,f])
#            D=np.array(result) 
#            #print D
#            
#            #calculate DFT using Euler's Formula to replace exp with sin and cos
#            result1=[]
#            for k in range(D.shape[0]):
#                PI=math.pi 
#                DFT2=0
#                a=0
#                b=0
#                for i in range(Data.shape[0]):
#                    J=D[k,0]
#                    F=D[k,1]
#                    t=Data[i,0]
#                    x=Data[i,1]
#                    c=2*PI*F*t
#                    ae=x*(math.cos(c))
#                    be=x*(math.sin(c))
#                    a=a+ae
#                    b=b+be
#                    DFT2=a**2 + b**2
#                result1.append([J,F,DFT2])
#            DFT=np.array(result1)
#            #calculate the PSD value for each frequency
#            result2=[]
#            for n in range (DFT.shape[0]):
#                PSD=math.log10((2*(DFT[n,2])*dT/N))
#                Fj=math.log10((DFT[n,1]))
#                result2.append([n,Fj,PSD])
#            PSD=np.array(result2)
#            name2='PSD_'+('{}'.format(ua))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2 + name2 , PSD)
#        
#            result3=[]
#            LEN=len(PSD)
#            bin1=8
#            li=np.arange(0,LEN+1,bin1)
#            print LEN
#            k=len(li)-1
#            true_psd=0
#            mean_freq=0
#            err_true_psd=0
#            for p in range (li.shape[0]-1):
#                m=li[p]+bin1-1
#                k=li[p]
#                true_psd=PSD[k:m,2].mean()+0.20568
#                mean_freq=PSD[k:m,1].mean()
#                err_true_psd=0.31025/bin1
#                result3.append([mean_freq, true_psd, err_true_psd])
#            fit=np.array(result3)
#            print fit
##            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
##            print slope
#            print fit
#            print (fit.shape)
#            name3= 'PSD_Fit_'+('{}'.format(ua))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2+name3 , fit)   
            
           
#u1=23
#X=np.arange (1.0, 3.1, 0.2) 
#Z=np.arange(0,1.2, 0.005 )
#for y in range (X.shape[0]):
#    z=X[y]
#    for Y in range (Z.shape[0]):
#        w=Z[Y]
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u1))+'GHz/'+('{}'.format(u1))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'
#        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'+('{}'.format(u1))+'_PSD_sim/'+('{}'.format(u1))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        #route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'
#        if not os.path.isdir(route1):
#            os.makedirs(route1)
#        if not os.path.isdir(route2):
#            os.makedirs(route2)
#        for o in range (1,101): 
#            name1= ('{}'.format(u1))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(o))+'.dat'
#            Data=np.loadtxt(route1+name1)
#            A=Data[0,0]
#            dT=Data[1,0]-A
#            #get the number of lines in the data file
#            #N=sum(1 for row in Data)
#            # or N=sum(1 for line in Data)
#            #or simply write
#            N=len(Data)
#            #get the period of Data
#            #generate an array for the j values
#            L=np.arange(1, N/2, 1)
#            #create an array with j and corresponding frequency in an array
#            result =[]
#            for m in range(L.shape[0]):
#                j=L[m]
#                f=j/(N*dT)
#                result.append([j,f])
#            D=np.array(result) 
#            #print D
#            
#            #calculate DFT using Euler's Formula to replace exp with sin and cos
#            result1=[]
#            for k in range(D.shape[0]):
#                PI=math.pi 
#                DFT2=0
#                a=0
#                b=0
#                for i in range(Data.shape[0]):
#                    J=D[k,0]
#                    F=D[k,1]
#                    t=Data[i,0]
#                    x=Data[i,1]
#                    c=2*PI*F*t
#                    ae=x*(math.cos(c))
#                    be=x*(math.sin(c))
#                    a=a+ae
#                    b=b+be
#                    DFT2=a**2 + b**2
#                result1.append([J,F,DFT2])
#            DFT=np.array(result1)
#            #calculate the PSD value for each frequency
#            result2=[]
#            for n in range (DFT.shape[0]):
#                PSD=math.log10((2*(DFT[n,2])*dT/N))
#                Fj=math.log10((DFT[n,1]))
#                result2.append([n,Fj,PSD])
#            PSD=np.array(result2)
#            name2='PSD_'+('{}'.format(u1))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2 + name2 , PSD)
#        
#            result3=[]
#            LEN=len(PSD)
#            bin1=8
#            li=np.arange(0,LEN+1,bin1)
#            print LEN
#            k=len(li)-1
#            true_psd=0
#            mean_freq=0
#            err_true_psd=0
#            for p in range (li.shape[0]-1):
#                m=li[p]+bin1-1
#                k=li[p]
#                true_psd=PSD[k:m,2].mean()+0.20568
#                mean_freq=PSD[k:m,1].mean()
#                err_true_psd=0.31025/bin1
#                result3.append([mean_freq, true_psd, err_true_psd])
#            fit=np.array(result3)
#            print fit
##            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
##            print slope
#            print fit
#            print (fit.shape)
#            name3= 'PSD_Fit_'+('{}'.format(u1))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2+name3 , fit)  
#            
#
#u2=32
#X=np.arange (1.0, 3.1, 0.2) 
#Z=np.arange(0,1.2, 0.005 )
#for y in range (X.shape[0]):
#    z=X[y]
#    for Y in range (Z.shape[0]):
#        w=Z[Y]
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u2))+'GHz/'+('{}'.format(u2))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'
#        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'+('{}'.format(u2))+'_PSD_sim/'+('{}'.format(u2))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        #route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'
#        if not os.path.isdir(route1):
#            os.makedirs(route1)
#        if not os.path.isdir(route2):
#            os.makedirs(route2)
#        for o in range (1,101): 
#            name1= ('{}'.format(u2))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(o))+'.dat'
#            Data=np.loadtxt(route1+name1)
#            A=Data[0,0]
#            dT=Data[1,0]-A
#            #get the number of lines in the data file
#            #N=sum(1 for row in Data)
#            # or N=sum(1 for line in Data)
#            #or simply write
#            N=len(Data)
#            #get the period of Data
#            #generate an array for the j values
#            L=np.arange(1, N/2, 1)
#            #create an array with j and corresponding frequency in an array
#            result =[]
#            for m in range(L.shape[0]):
#                j=L[m]
#                f=j/(N*dT)
#                result.append([j,f])
#            D=np.array(result) 
#            #print D
#            
#            #calculate DFT using Euler's Formula to replace exp with sin and cos
#            result1=[]
#            for k in range(D.shape[0]):
#                PI=math.pi 
#                DFT2=0
#                a=0
#                b=0
#                for i in range(Data.shape[0]):
#                    J=D[k,0]
#                    F=D[k,1]
#                    t=Data[i,0]
#                    x=Data[i,1]
#                    c=2*PI*F*t
#                    ae=x*(math.cos(c))
#                    be=x*(math.sin(c))
#                    a=a+ae
#                    b=b+be
#                    DFT2=a**2 + b**2
#                result1.append([J,F,DFT2])
#            DFT=np.array(result1)
#            #calculate the PSD value for each frequency
#            result2=[]
#            for n in range (DFT.shape[0]):
#                PSD=math.log10((2*(DFT[n,2])*dT/N))
#                Fj=math.log10((DFT[n,1]))
#                result2.append([n,Fj,PSD])
#            PSD=np.array(result2)
#            name2='PSD_'+('{}'.format(u2))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2 + name2 , PSD)
#        
#            result3=[]
#            LEN=len(PSD)
#            bin1=8
#            li=np.arange(0,LEN+1,bin1)
#            print LEN
#            k=len(li)-1
#            true_psd=0
#            mean_freq=0
#            err_true_psd=0
#            for p in range (li.shape[0]-1):
#                m=li[p]+bin1-1
#                k=li[p]
#                true_psd=PSD[k:m,2].mean()+0.20568
#                mean_freq=PSD[k:m,1].mean()
#                err_true_psd=0.31025/bin1
#                result3.append([mean_freq, true_psd, err_true_psd])
#            fit=np.array(result3)
#            print fit
##            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
##            print slope
#            print fit
#            print (fit.shape)
#            name3= 'PSD_Fit_'+('{}'.format(u2))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2+name3 , fit)  
#    
#u3=86
#X=np.arange (1.0, 3.1, 0.2) 
#Z=np.arange(0,1.2, 0.005 )
#for y in range (X.shape[0]):
#    z=X[y]
#    for Y in range (Z.shape[0]):
#        w=Z[Y]
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u3))+'GHz/'+('{}'.format(u3))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'
#        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'+('{}'.format(u3))+'_PSD_sim/'+('{}'.format(u3))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        #route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'
#        if not os.path.isdir(route1):
#            os.makedirs(route1)
#        if not os.path.isdir(route2):
#            os.makedirs(route2)
#        for o in range (1,101): 
#            name1= ('{}'.format(u3))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(o))+'.dat'
#            Data=np.loadtxt(route1+name1)
#            A=Data[0,0]
#            dT=Data[1,0]-A
#            #get the number of lines in the data file
#            #N=sum(1 for row in Data)
#            # or N=sum(1 for line in Data)
#            #or simply write
#            N=len(Data)
#            #get the period of Data
#            #generate an array for the j values
#            L=np.arange(1, N/2, 1)
#            #create an array with j and corresponding frequency in an array
#            result =[]
#            for m in range(L.shape[0]):
#                j=L[m]
#                f=j/(N*dT)
#                result.append([j,f])
#            D=np.array(result) 
#            #print D
#            
#            #calculate DFT using Euler's Formula to replace exp with sin and cos
#            result1=[]
#            for k in range(D.shape[0]):
#                PI=math.pi 
#                DFT2=0
#                a=0
#                b=0
#                for i in range(Data.shape[0]):
#                    J=D[k,0]
#                    F=D[k,1]
#                    t=Data[i,0]
#                    x=Data[i,1]
#                    c=2*PI*F*t
#                    ae=x*(math.cos(c))
#                    be=x*(math.sin(c))
#                    a=a+ae
#                    b=b+be
#                    DFT2=a**2 + b**2
#                result1.append([J,F,DFT2])
#            DFT=np.array(result1)
#            #calculate the PSD value for each frequency
#            result2=[]
#            for n in range (DFT.shape[0]):
#                PSD=math.log10((2*(DFT[n,2])*dT/N))
#                Fj=math.log10((DFT[n,1]))
#                result2.append([n,Fj,PSD])
#            PSD=np.array(result2)
#            name2='PSD_'+('{}'.format(u3))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2 + name2 , PSD)
#        
#            result3=[]
#            LEN=len(PSD)
#            bin1=8
#            li=np.arange(0,LEN+1,bin1)
#            print LEN
#            k=len(li)-1
#            true_psd=0
#            mean_freq=0
#            err_true_psd=0
#            for p in range (li.shape[0]-1):
#                m=li[p]+bin1-1
#                k=li[p]
#                true_psd=PSD[k:m,2].mean()+0.20568
#                mean_freq=PSD[k:m,1].mean()
#                err_true_psd=0.31025/bin1
#                result3.append([mean_freq, true_psd, err_true_psd])
#            fit=np.array(result3)
#            print fit
##            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
##            print slope
#            print fit
#            print (fit.shape)
#            name3= 'PSD_Fit_'+('{}'.format(u3))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2+name3 , fit)
#            
#u4=230
#X=np.arange (1.0, 3.1, 0.2) 
#Z=np.arange(0,1.2, 0.005 )
#for y in range (X.shape[0]):
#    z=X[y]
#    for Y in range (Z.shape[0]):
#        w=Z[Y]
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u4))+'GHz/'+('{}'.format(u4))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'
#        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'+('{}'.format(u4))+'_PSD_sim/'+('{}'.format(u4))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        #route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'
#        if not os.path.isdir(route1):
#            os.makedirs(route1)
#        if not os.path.isdir(route2):
#            os.makedirs(route2)
#        for o in range (1,101): 
#            name1= ('{}'.format(u4))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(o))+'.dat'
#            Data=np.loadtxt(route1+name1)
#            A=Data[0,0]
#            dT=Data[7,0]-A
#            #print dT
#            #get the number of lines in the data file
#            #N=sum(1 for row in Data)
#            # or N=sum(1 for line in Data)
#            #or simply write
#            N=len(Data)
#            #get the period of Data
#            #generate an array for the j values
#            L=np.arange(1, N/2, 1)
#            #create an array with j and corresponding frequency in an array
#            result =[]
#            for m in range(L.shape[0]):
#                j=L[m]
#                f=j/(N*dT)
#                result.append([j,f])
#            D=np.array(result) 
#            #print D
#            
#            #calculate DFT using Euler's Formula to replace exp with sin and cos
#            result1=[]
#            for k in range(D.shape[0]):
#                PI=math.pi 
#                DFT2=0
#                a=0
#                b=0
#                for i in range(Data.shape[0]):
#                    J=D[k,0]
#                    F=D[k,1]
#                    t=Data[i,0]
#                    x=Data[i,1]
#                    c=2*PI*F*t
#                    ae=x*(math.cos(c))
#                    be=x*(math.sin(c))
#                    a=a+ae
#                    b=b+be
#                    DFT2=a**2 + b**2
#                result1.append([J,F,DFT2])
#            DFT=np.array(result1)
#            #calculate the PSD value for each frequency
#            result2=[]
#            for n in range (DFT.shape[0]):
#                PSD=math.log10((2*(DFT[n,2])*dT/N))
#                Fj=math.log10((DFT[n,1]))
#                result2.append([n,Fj,PSD])
#            PSD=np.array(result2)
#            name2='PSD_'+('{}'.format(u4))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2 + name2 , PSD)
#        
#            result3=[]
#            LEN=len(PSD)
#            bin1=8
#            li=np.arange(0,LEN+1,bin1)
#            print LEN
#            k=len(li)-1
#            true_psd=0
#            mean_freq=0
#            err_true_psd=0
#            for p in range (li.shape[0]-1):
#                m=li[p]+bin1-1
#                k=li[p]
#                true_psd=PSD[k:m,2].mean()+0.20568
#                mean_freq=PSD[k:m,1].mean()
#                err_true_psd=0.31025/bin1
#                result3.append([mean_freq, true_psd, err_true_psd])
#            fit=np.array(result3)
#            print fit
##            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
##            print slope
#            print fit
#            print (fit.shape)
#            name3= 'PSD_Fit_'+('{}'.format(u4))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2+name3 , fit)
#            
#            
#            
#u5=142
#X=np.arange (2.0, 2.1, 0.2) 
#Z=np.arange(0.05,5, 0.05 )
#for y in range (X.shape[0]):
#    z=X[y]
#    for Y in range (Z.shape[0]):
#        w=Z[Y]
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u5))+'GHz/'+('{}'.format(u5))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'
#        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'+('{}'.format(u5))+'_PSD_sim/'+('{}'.format(u5))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        #route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'
#        if not os.path.isdir(route1):
#            os.makedirs(route1)
#        if not os.path.isdir(route2):
#            os.makedirs(route2)
#        for o in range (1,201): 
#            name1= ('{}'.format(u5))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(o))+'.dat'
#            Data=np.loadtxt(route1+name1)
#            A=Data[0,0]
#            dT=Data[1,0]-A
#            #get the number of lines in the data file
#            #N=sum(1 for row in Data)
#            # or N=sum(1 for line in Data)
#            #or simply write
#            N=len(Data)
#            #get the period of Data
#            #generate an array for the j values
#            L=np.arange(1, N/2, 1)
#            #create an array with j and corresponding frequency in an array
#            result =[]
#            for m in range(L.shape[0]):
#                j=L[m]
#                f=j/(N*dT)
#                result.append([j,f])
#            D=np.array(result) 
#            #print D
#            
#            #calculate DFT using Euler's Formula to replace exp with sin and cos
#            result1=[]
#            for k in range(D.shape[0]):
#                PI=math.pi 
#                DFT2=0
#                a=0
#                b=0
#                for i in range(Data.shape[0]):
#                    J=D[k,0]
#                    F=D[k,1]
#                    t=Data[i,0]
#                    x=Data[i,1]
#                    c=2*PI*F*t
#                    ae=x*(math.cos(c))
#                    be=x*(math.sin(c))
#                    a=a+ae
#                    b=b+be
#                    DFT2=a**2 + b**2
#                result1.append([J,F,DFT2])
#            DFT=np.array(result1)
#            #calculate the PSD value for each frequency
#            result2=[]
#            for n in range (DFT.shape[0]):
#                PSD=math.log10((2*(DFT[n,2])*dT/N))
#                Fj=math.log10((DFT[n,1]))
#                result2.append([n,Fj,PSD])
#            PSD=np.array(result2)
#            name2='PSD_'+('{}'.format(u5))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2 + name2 , PSD)
#        
#            result3=[]
#            LEN=len(PSD)
#            bin1=8
#            li=np.arange(0,LEN+1,bin1)
#            print LEN
#            k=len(li)-1
#            true_psd=0
#            mean_freq=0
#            err_true_psd=0
#            for p in range (li.shape[0]-1):
#                m=li[p]+bin1-1
#                k=li[p]
#                true_psd=PSD[k:m,2].mean()+0.20568
#                mean_freq=PSD[k:m,1].mean()
#                err_true_psd=0.31025/bin1
#                result3.append([mean_freq, true_psd, err_true_psd])
#            fit=np.array(result3)
#            print fit
##            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
##            print slope
#            print fit
#            print (fit.shape)
#            name3= 'PSD_Fit_'+('{}'.format(u5))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2+name3 , fit)