# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:25:39 2015

@author: celine
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:24:52 2015

@author: celine
"""

import numpy as np
import math as m
from scipy import interpolate
import matplotlib.pyplot as plt
#import the data files
route1= '/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Used_Data/'
route2= '/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_File/'
u=230
#name1= ('{}'.format(u))+'GHz.dat' 
name1='Jflx_inter.dat'
Da=np.loadtxt(route1+name1)
n= len(Da)
sampling=[]
for i in range (Da.shape[0]-1):
    st=Da[i+1,0]-Da[i,0]
    sampling.append([st])
sam=np.array(sampling)
bin = int(sam.min()) 
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
nameint='Jflx_inter.dat'
np.savetxt(route1+nameint, Data1)


#plt.plot(x,y ,'o', xnew , f, '-')
#plt.show()
Data1[0,1]=0
A=Data1[0,0]
dT=Data1[1,0]-A
print dT
mean=Data1[:,1].mean()
DATA=[]
for l in range(Data1.shape[0]):
    T=Data1[l,0]-A
    F=Data1[l,1]-mean
#    e1=Data1[l,2]
#    e2=Data1[l,3]
    DATA.append([T,F])
Data=np.array(DATA)
#print Data
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
    p=m.pi
    DFT2=0
    a=0
    b=0
    for i in range(Data.shape[0]):
        J=D[k,0]
        F=D[k,1]
        t=Data[i,0]
        x=Data[i,1]
        c=2*p*F*t
        ae=x*(m.cos(c))
        be=x*(m.sin(c))
        a=a+ae
        b=b+be
        DFT2=a**2 + b**2
    result1.append([J,F,DFT2])
DFT=np.array(result1)
#calculate the PSD value for each frequency
result2=[]
for l in range (DFT.shape[0]):
    PSD=m.log10((2*(DFT[l,2])*dT/N))
    Fj=m.log10((DFT[l,1]))
    result2.append([l,Fj,PSD])
PSD=np.array(result2)
route2='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/PSD_File/'
#name2='PSD_'+('{}'.format(u))+'_inter.dat'
name2="PSD_Jflx_inter.dat"
np.savetxt(route2+name2 , PSD)

result3=[]
n=len(PSD)
bin1=8
l=np.arange(0,n+1,bin1)
print n
k=len(l)-1
true_psd=0
mean_freq=0
err_true_psd=0
for j in range (l.shape[0]-1):
    m=l[j]+bin1-1
    k=l[j]
    true_psd=PSD[k:m,2].mean()+0.20568
    mean_freq=PSD[k:m,1].mean()
    err_true_psd=0.31025/bin1
    result3.append([mean_freq, true_psd, err_true_psd])
fit=np.array(result3)
print fit
slope=(fit[1,1]-fit[0,1])/(fit[1,0]-fit[0,0])
print slope
#print fit
#print (fit.shape)
#print slope
#name3= 'PSD_Fit'+('{}'.format(u))+'_inter.dat' 
name3="PSD_Fit_Jflx_inter.dat"
np.savetxt(route2+name3 , fit)