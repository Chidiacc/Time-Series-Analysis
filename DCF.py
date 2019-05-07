# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:24:52 2015

@author: celine
"""

import numpy as np
import math
import os
#import the data files
#set a time range for the data
#calculate the mean values and the standard deviation
#load the first data file
route1 = "/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Used_Data/"
name1 = '230GHz.dat'
DataIn1full=np.loadtxt(route1+name1)
st=DataIn1full[:,1].std()
print st
file1 = []
sta=0
time= 2454000+600
time1=2454000+1600
for sta in range(DataIn1full.shape[0]):
    if ((sta < len(DataIn1full)) and (DataIn1full[sta,0]>time) and (DataIn1full[sta,0]<time1)):
        t=DataIn1full[sta,0]
        da=DataIn1full[sta,1]
        e=DataIn1full[sta,2]
        sta=sta+1
        file1.append([t,da,e])
    DataIn1=np.array(file1)
mean1=DataIn1[: ,1].mean()
sd1=DataIn1[: ,1].std()



#load the second data file 
#calculate mean and standard deviation   
route2 = '/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Used_Data/'
name2 = '230GHz.dat'
DataIn2full=np.loadtxt(route2+name2)
file2 = []
stb=0
for stb in range(DataIn2full.shape[0]):
    if ((stb < len(DataIn2full)) and (DataIn2full[stb,0]>time) and (DataIn2full[stb,0]<time1)):
        t2=DataIn2full[stb,0]
        da2=DataIn2full[stb,1]
        #e2=DataIn2full[stb,2]
        stb=stb+1
        file2.append([t2,da2])
    DataIn2=np.array(file2)
mean2=DataIn2[:,1].mean()
sd2=DataIn2[:,1].std()

#Calculate the UDCF
result=[]
for i in range(DataIn1.shape[0]):
    for j in range(DataIn2.shape[0]):
        d=(DataIn1[i,1]-mean1)*(DataIn2[j,1]-mean2)
        a=(sd1**2)
        b=(sd2**2)
        e=a*b
        c=np.sqrt(e)
        udcf=d/c
        dt= DataIn2[j,0] - DataIn1[i,0]
        int(dt)
        result.append([dt, udcf])
        
#sort results in order
result= sorted(result, key=lambda a: a[0])
UDCF=np.array(result)
name1='UDCF.dat' 
np.savetxt(route1+name1 , UDCF)

#bin the time values
#set a range for the time lags
bin=5
l=np.arange(-700,701,bin)
Data=[]
#get the Data in an array
#get the number of data point in each bin
statement=0
for m in range(l.shape[0]):
    n=m+1
    M=0
    S=0
    dcf=0
    #get the loop to run starting from the previous statement
    #Calculate the DCF
    while (statement < len(UDCF)) and (UDCF[statement,0]<l[m]):
        Dt=UDCF[statement, 0]
        H=UDCF[statement,1]
        statement = statement +1
        M=M+1;
        S=S+H;
        dcf=S/M
    Data.append([M,S,dcf])
MU=np.array(Data)

#calculate the error on the DCF values
DAta=[]
statement1=0
for z in range(l.shape[0]):
    y=z+1
    p=0
    q=0
    s=0
    N=0
    while (statement1 < len(UDCF)) and (UDCF[statement1, 0]<l[z]):
        Dt=UDCF[statement1, 0]
        H=UDCF[statement1,1]
        statement1 = statement1 +1
        Dc=MU[z,2]
        N=MU[z,0]-1
        p=(H-Dc)**2
        s=s+p
        q=math.sqrt(s)
    DAta.append([N,q])
MU1=np.array(DAta)

#get the error on the time bin
DATA=[]
for o in range(MU.shape[0]):
    ter=bin/2
    tl=l[o]-ter
    DT=MU[o,2]
    er=MU1[o,1]/MU1[o,0]    
    DATA.append([tl,DT,ter,er])
DCF=np.array(DATA)
print (DCF.shape)
Route='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Discrete_Correlation_Function/'
if not os.path.isdir(Route):
    os.makedirs(Route)
NAME='DCF_230vs230_'+('{}'.format(bin))+'_fulldata.dat'
np.savetxt(Route+NAME, DCF)