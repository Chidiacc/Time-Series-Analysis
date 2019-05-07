# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:28:04 2015

@author: chidiac
"""

import numpy as np



a=1.05
b=0.9*a

tl=np.ones(41)*b
c=np.arange(-50,401,20)

result=[]
for i in range (c.shape[0]):
    r=c[i]
    T=tl[i]
    result.append([r,T])
re=np.array(result)

print re

route='/media/My Passport/DOCUMENTS/Masterarbeit/Discrete_Correlation_Function/'
name='90per_DCFvalue.dat'
np.savetxt(route+name, re)