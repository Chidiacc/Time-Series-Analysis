# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:45:48 2015

@author: chidiac
"""

import numpy as np

route='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/'
route2= '/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/chi_sqaure_test/'

name1="Chi_Square_Vflx_1.0.dat"
name2="Chi_Square_Vflx_1.2.dat"
name3="Chi_Square_Vflx_1.4.dat"
name4="Chi_Square_Vflx_1.6.dat"
name5="Chi_Square_Vflx_1.8.dat"
name5="Chi_Square_Vflx_2.0.dat"
name6="Chi_Square_Vflx_2.2.dat"
name7="Chi_Square_Vflx_2.4.dat"
name8="Chi_Square_Vflx_2.6.dat"
name9="Chi_Square_Vflx_2.8.dat"
name10="Chi_Square_Vflx_3.0.dat"
#z=350
#name1="Chi_Square_"+('{}'.format(z))+"_1.0.dat"
#name2="Chi_Square_"+('{}'.format(z))+"_1.2.dat"
#name3="Chi_Square_"+('{}'.format(z))+"_1.4.dat"
#name4="Chi_Square_"+('{}'.format(z))+"_1.6.dat"
#name5="Chi_Square_"+('{}'.format(z))+"_1.8.dat"
#name5="Chi_Square_"+('{}'.format(z))+"_2.0.dat"
#name6="Chi_Square_"+('{}'.format(z))+"_2.2.dat"
#name7="Chi_Square_"+('{}'.format(z))+"_2.4.dat"
#name8="Chi_Square_"+('{}'.format(z))+"_2.6.dat"
#name9="Chi_Square_"+('{}'.format(z))+"_2.8.dat"
#name10="Chi_Square_"+('{}'.format(z))+"_3.0.dat"
chi1=np.loadtxt(route2+name1)
chi2=np.loadtxt(route2+name2)
chi3=np.loadtxt(route2+name3)
chi4=np.loadtxt(route2+name4)
chi5=np.loadtxt(route2+name5)
chi6=np.loadtxt(route2+name6)
chi7=np.loadtxt(route2+name7)
chi8=np.loadtxt(route2+name8)
chi9=np.loadtxt(route2+name9)
chi10=np.loadtxt(route2+name10)




m1=min(chi1[:,1])

print 'm1=', m1 

ind=np.argmin(chi1[:,1])

i= chi1[ind,0]

print 'i1=' , i

m2=min(chi2[:,1])

print 'm2=', m2

ind2=np.argmin(chi2[:,1])

i2= chi2[ind,0]

print 'i2=' , i2

m3=min(chi3[:,1])

print 'm3=', m3

ind3=np.argmin(chi3[:,1])

i3= chi3[ind,0]

print 'i3=' , i3

m4=min(chi4[:,1])

print 'm4=', m4

ind4=np.argmin(chi4[:,1])

i4= chi4[ind,0]

print 'i4=' , i4

m5=min(chi5[:,1])

print 'm5=', m5

ind5=np.argmin(chi5[:,1])

i5= chi5[ind,0]

print 'i5=' , i5

m6=min(chi6[:,1])

print 'm6=', m6

ind6=np.argmin(chi6[:,1])

i6= chi6[ind,0]

print 'i6=' , i6

m7=min(chi7[:,1])

print 'm7=', m7

ind7=np.argmin(chi7[:,1])

i7= chi7[ind,0]

print 'i7=' , i7

m8=min(chi8[:,1])

print 'm8=', m8

ind8=np.argmin(chi8[:,1])

i8= chi8[ind,0]

print 'i8=' , i8

m9=min(chi9[:,1])

print 'm9=', m9

ind9=np.argmin(chi9[:,1])

i9= chi9[ind,0]

print 'i9=' , i9

m10=min(chi10[:,1])

print 'm10=', m10

ind10=np.argmin(chi10[:,1])

i10= chi10[ind,0]

print 'i10=' , i10

minimum= min(m1, m2, m3, m4, m5, m6, m7, m8, m9, m10)

print 'minimum =' , minimum

