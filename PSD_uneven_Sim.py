## -*- coding: utf-8 -*-
#"""
#Created on Mon Jul 13 13:52:57 2015
#
#@author: chidiac
#"""
#
import numpy as np
import math 
import os
from scipy import interpolate

##import the data files
#u=2.6
#X=np.arange (1.0, 3.1, 0.2) 
#Z=np.arange(0,1.2, 0.005 )
#for y in range (X.shape[0]):
#    z=X[y]
#    for Y in range (Z.shape[0]):
#        w=Z[Y]
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u))+'GHz/'+('{}'.format(u))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'
#        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'+('{}'.format(u))+'_PSD_sim/'+('{}'.format(u))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
#        #route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'
#        if not os.path.isdir(route1):
#            os.makedirs(route1)
#        if not os.path.isdir(route2):
#            os.makedirs(route2)
#        for o in range (1,100): 
#            name1= ('{}'.format(u))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(o))+'.dat'
#            Da=np.loadtxt(route1+name1)
#            LE= len(Da)
#            sampling=[]
#            for i in range (Da.shape[0]-1):
#                st=Da[i+1,0]-Da[i,0]
#                sampling.append([st])
#            sam=np.array(sampling)
#            bin = int(sam.mean()) 
#            print bin  
#            result=[]
#            x=Da[:,0]
#            y=Da[:,1]
#            xnew=np.arange(x.min() , x.max(),bin)
#            f=interpolate.interp1d(x,y)(xnew)
#            inter=[]
#            for j in range (xnew.shape[0]):
#                xn=xnew[j]
#                fn=f[j]
#                inter.append([xn,fn])
#            Data1=np.array(inter)
#            Data1[0,1]=0
#            A=Data1[0,0]
#            dT=Data1[1,0]-A
#            mean=Data1[:,1].mean()
#            DATA=[]
#            for l in range(Data1.shape[0]):
#                T=Data1[l,0]-A
#                F=Data1[l,1]-mean
#                #    e1=Data1[l,2]
#                #    e2=Data1[l,3]
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
#            name2='PSD_'+('{}'.format(u))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
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
#            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
#            print slope
#            print fit
#            print (fit.shape)
#            name3= 'PSD_Fit_'+('{}'.format(u))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2+name3 , fit)
#    
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
#            Da=np.loadtxt(route1+name1)
#            LE= len(Da)
#            sampling=[]
#            for i in range (Da.shape[0]-1):
#                st=Da[i+1,0]-Da[i,0]
#                sampling.append([st])
#            sam=np.array(sampling)
#            bin = int(sam.mean()) 
#            print bin  
#            result=[]
#            x=Da[:,0]
#            y=Da[:,1]
#            xnew=np.arange(x.min() , x.max(),bin)
#            f=interpolate.interp1d(x,y)(xnew)
#            inter=[]
#            for j in range (xnew.shape[0]):
#                xn=xnew[j]
#                fn=f[j]
#                inter.append([xn,fn])
#            Data1=np.array(inter)
#            Data1[0,1]=0
#            A=Data1[0,0]
#            dT=Data1[1,0]-A
#            mean=Data1[:,1].mean()
#            DATA=[]
#            for l in range(Data1.shape[0]):
#                T=Data1[l,0]-A
#                F=Data1[l,1]-mean
#                #    e1=Data1[l,2]
#                #    e2=Data1[l,3]
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
#            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
#            print slope
#            print fit
#            print (fit.shape)
#            name3= 'PSD_Fit_'+('{}'.format(u1))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
#            np.savetxt(route2+name3 , fit)
#            
    
u2=32
X=np.arange (1.0, 3.1, 0.2) 
Z=np.arange(0,1.2, 0.005 )
for y in range (X.shape[0]):
    z=X[y]
    for Y in range (Z.shape[0]):
        w=Z[Y]
        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u2))+'GHz/'+('{}'.format(u2))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'
        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'+('{}'.format(u2))+'_PSD_sim/'+('{}'.format(u2))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
        #route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'
        if not os.path.isdir(route1):
            os.makedirs(route1)
        if not os.path.isdir(route2):
            os.makedirs(route2)
        for o in range (1,101): 
            name1= ('{}'.format(u2))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(o))+'.dat'
            Da=np.loadtxt(route1+name1)
            LE= len(Da)
            sampling=[]
            for i in range (Da.shape[0]-1):
                st=Da[i+1,0]-Da[i,0]
                sampling.append([st])
            sam=np.array(sampling)
            bin = int(sam.mean()) 
            print bin  
            result=[]
            x=Da[:,0]
            y=Da[:,1]
            xnew=np.arange(x.min() , x.max(),bin)
            f=interpolate.interp1d(x,y)(xnew)
            inter=[]
            for j in range (xnew.shape[0]):
                xn=xnew[j]
                fn=f[j]
                inter.append([xn,fn])
            Data1=np.array(inter)
            Data1[0,1]=0
            A=Data1[0,0]
            dT=Data1[1,0]-A
            mean=Data1[:,1].mean()
            DATA=[]
            for l in range(Data1.shape[0]):
                T=Data1[l,0]-A
                F=Data1[l,1]-mean
                #    e1=Data1[l,2]
                #    e2=Data1[l,3]
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
            for m in range(L.shape[0]):
                j=L[m]
                f=j/(N*dT)
                result.append([j,f])
            D=np.array(result) 
            #print D
            
            #calculate DFT using Euler's Formula to replace exp with sin and cos
            result1=[]
            for k in range(D.shape[0]):
                PI=math.pi 
                DFT2=0
                a=0
                b=0
                for i in range(Data.shape[0]):
                    J=D[k,0]
                    F=D[k,1]
                    t=Data[i,0]
                    x=Data[i,1]
                    c=2*PI*F*t
                    ae=x*(math.cos(c))
                    be=x*(math.sin(c))
                    a=a+ae
                    b=b+be
                    DFT2=a**2 + b**2
                result1.append([J,F,DFT2])
            DFT=np.array(result1)
            #calculate the PSD value for each frequency
            result2=[]
            for n in range (DFT.shape[0]):
                PSD=math.log10((2*(DFT[n,2])*dT/N))
                Fj=math.log10((DFT[n,1]))
                result2.append([n,Fj,PSD])
            PSD=np.array(result2)
            name2='PSD_'+('{}'.format(u2))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
            np.savetxt(route2 + name2 , PSD)
        
            result3=[]
            LEN=len(PSD)
            bin1=8
            li=np.arange(0,LEN+1,bin1)
            print LEN
            k=len(li)-1
            true_psd=0
            mean_freq=0
            err_true_psd=0
            for p in range (li.shape[0]-1):
                m=li[p]+bin1-1
                k=li[p]
                true_psd=PSD[k:m,2].mean()+0.20568
                mean_freq=PSD[k:m,1].mean()
                err_true_psd=0.31025/bin1
                result3.append([mean_freq, true_psd, err_true_psd])
            fit=np.array(result3)
            print fit
#            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
#            print slope
#            print fit
#            print (fit.shape)
            name3= 'PSD_Fit_'+('{}'.format(u2))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
            np.savetxt(route2+name3 , fit)
            
    
u3=86
X=np.arange (1.0, 3.1, 0.2) 
Z=np.arange(0,1.2, 0.005 )
for y in range (X.shape[0]):
    z=X[y]
    for Y in range (Z.shape[0]):
        w=Z[Y]
        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u3))+'GHz/'+('{}'.format(u3))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'
        route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'+('{}'.format(u3))+'_PSD_sim/'+('{}'.format(u3))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/' 
        #route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_sim/'
        if not os.path.isdir(route1):
            os.makedirs(route1)
        if not os.path.isdir(route2):
            os.makedirs(route2)
        for o in range (1,101): 
            name1= ('{}'.format(u3))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(o))+'.dat'
            Da=np.loadtxt(route1+name1)
            LE= len(Da)
            sampling=[]
            for i in range (Da.shape[0]-1):
                st=Da[i+1,0]-Da[i,0]
                sampling.append([st])
            sam=np.array(sampling)
            bin = int(sam.mean()) 
            print bin  
            result=[]
            x=Da[:,0]
            y=Da[:,1]
            xnew=np.arange(x.min() , x.max(),bin)
            f=interpolate.interp1d(x,y)(xnew)
            inter=[]
            for j in range (xnew.shape[0]):
                xn=xnew[j]
                fn=f[j]
                inter.append([xn,fn])
            Data1=np.array(inter)
            Data1[0,1]=0
            A=Data1[0,0]
            dT=Data1[1,0]-A
            mean=Data1[:,1].mean()
            DATA=[]
            for l in range(Data1.shape[0]):
                T=Data1[l,0]-A
                F=Data1[l,1]-mean
                #    e1=Data1[l,2]
                #    e2=Data1[l,3]
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
            for m in range(L.shape[0]):
                j=L[m]
                f=j/(N*dT)
                result.append([j,f])
            D=np.array(result) 
            #print D
            
            #calculate DFT using Euler's Formula to replace exp with sin and cos
            result1=[]
            for k in range(D.shape[0]):
                PI=math.pi 
                DFT2=0
                a=0
                b=0
                for i in range(Data.shape[0]):
                    J=D[k,0]
                    F=D[k,1]
                    t=Data[i,0]
                    x=Data[i,1]
                    c=2*PI*F*t
                    ae=x*(math.cos(c))
                    be=x*(math.sin(c))
                    a=a+ae
                    b=b+be
                    DFT2=a**2 + b**2
                result1.append([J,F,DFT2])
            DFT=np.array(result1)
            #calculate the PSD value for each frequency
            result2=[]
            for n in range (DFT.shape[0]):
                PSD=math.log10((2*(DFT[n,2])*dT/N))
                Fj=math.log10((DFT[n,1]))
                result2.append([n,Fj,PSD])
            PSD=np.array(result2)
            name2='PSD_'+('{}'.format(u3))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
            np.savetxt(route2 + name2 , PSD)
        
            result3=[]
            LEN=len(PSD)
            bin1=8
            li=np.arange(0,LEN+1,bin1)
            print LEN
            k=len(li)-1
            true_psd=0
            mean_freq=0
            err_true_psd=0
            for p in range (li.shape[0]-1):
                m=li[p]+bin1-1
                k=li[p]
                true_psd=PSD[k:m,2].mean()+0.20568
                mean_freq=PSD[k:m,1].mean()
                err_true_psd=0.31025/bin1
                result3.append([mean_freq, true_psd, err_true_psd])
            fit=np.array(result3)
            print fit
            slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
            print slope
            print fit
            print (fit.shape)
            name3= 'PSD_Fit_'+('{}'.format(u3))+'_'+('{}'.format(z))+'_A'+('{}'.format(w))+'sim'+('{}'.format(o))+'.dat'
            np.savetxt(route2+name3 , fit)