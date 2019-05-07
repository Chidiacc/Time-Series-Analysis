import numpy as np
from DELCgen import *
import os


#u=142
## File Route
#route = "/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Used_Data/" 
#datfile = "Soft-Xray2to10KeV.dat"
#Da=np.loadtxt(route+datfile)
#sta=0
#sampling=[]
#for j in range (Da.shape[0]-1):
#    sta=Da[j+1,0]-Da[j,0]
#    sampling.append([sta])
#    sam=np.array(sampling)
#    b = int(sam.mean())
#
## PSD params
#v_bend=0.00127047657859
#c=0 
#
## Probability density function params 
#kappa,theta,lnmu,lnsig,weight1, weight2 = 16.0718341175, 0.706555433817, 1.92865231115, 0.0321306010236, 10.4722243039, -0.928652311151
#
## Simulation params 
#RedNoiseL,RandomSeed,aliasTbin, tbin = 100,12,1,b
#
## create mixture model (gamma and lognorm)
#model = Mixture_Dist([st.gamma,st.lognorm],[3,3],[[[2],[0]],[[2],[0],]])
#
## load data lightcurve 
#datalc = Load_Lightcurve(route+datfile,tbin) 
#
## estimate underlying variance of data light curve 
#datalc.STD_Estimate() 
#
#
#X=np.arange (1.8, 3.2, 0.2) 
#Z=np.arange(0.46,1.2, 0.005 ) 
#
#for y in range (X.shape[0]): 
#    z=X[y] 
#    print z
#    for Y in range (Z.shape[0]): 
#        w=Z[Y] 
#        print w
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/Soft-Xray2to10KeV/Soft-Xray2to10KeV_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/' 
#        if not os.path.isdir(route1): 
#            os.makedirs(route1) 
#        A= w        
#        a_low=z 
#        a_high = z 
#
#        for j in range(1, 21): 
#            print j
#
#            # simulate LC with params above
#            delc = Simulate_DE_Lightcurve(datalc,BendingPL, \
#                    (A,v_bend,a_low,a_high,c),model, \
#                        (kappa,theta,lnmu,lnsig,weight1,weight2),size=1, \
#                        RedNoiseL=RedNoiseL,randomSeed=RandomSeed, \
#                            aliasTbin=aliasTbin, LClength=None)
#
#
#            # save lc
#            name='Soft-Xray2to10KeVsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(j))+'.dat'
#            delc.Save_Lightcurve(os.path.join(route1, name))
#            

route = "/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Used_Data/" 
datfile = "Soft-Xray10to50KeV.dat"
Da=np.loadtxt(route+datfile)
sta=0
sampling=[]
for j in range (Da.shape[0]-1):
    sta=Da[j+1,0]-Da[j,0]
    sampling.append([sta])
    sam=np.array(sampling)
    b = int(sam.mean())

# PSD params
v_bend=0.00127047657859
c=0 

# Probability density function params 
kappa,theta,lnmu,lnsig,weight1, weight2 = 6.86805277675,  0.116380832612, -0.00820897650795, 0.300720731674, 2.29007796508, 1.00820897651

# Simulation params 
RedNoiseL,RandomSeed,aliasTbin, tbin = 100,12,1,b

# create mixture model (gamma and lognorm)
model = Mixture_Dist([st.gamma,st.lognorm],[3,3],[[[2],[0]],[[2],[0],]])

# load data lightcurve 
datalc = Load_Lightcurve(route+datfile,tbin) 

# estimate underlying variance of data light curve 
datalc.STD_Estimate() 


X=np.arange (1.0, 3.2, 0.2) 
Z=np.arange(0,1.2, 0.005 ) 

for y in range (X.shape[0]): 
    z=X[y] 
    print z
    for Y in range (Z.shape[0]): 
        w=Z[Y] 
        print w
        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/Soft-Xray10to50KeV/Soft-Xray10to50KeV_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/' 
        if not os.path.isdir(route1): 
            os.makedirs(route1) 
        A= w        
        a_low=z 
        a_high = z 

        for j in range(1, 21): 
            print j

            # simulate LC with params above
            delc = Simulate_DE_Lightcurve(datalc,BendingPL, \
                    (A,v_bend,a_low,a_high,c),model, \
                        (kappa,theta,lnmu,lnsig,weight1,weight2),size=1, \
                        RedNoiseL=RedNoiseL,randomSeed=RandomSeed, \
                            aliasTbin=aliasTbin, LClength=None)


            # save lc
            name='Soft-Xray10to50KeVsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(j))+'.dat'
            delc.Save_Lightcurve(os.path.join(route1, name))
            
            
#route = "/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Used_Data/" 
#datfile = "HardXray.dat"
#Da=np.loadtxt(route+datfile)
#sta=0
#sampling=[]
#for j in range (Da.shape[0]-1):
#    sta=Da[j+1,0]-Da[j,0]
#    sampling.append([sta])
#    sam=np.array(sampling)
#    b = int(sam.mean())
#
## PSD params
#v_bend=0.00127047657859
#c=0 
#
## Probability density function params 
#kappa,theta,lnmu,lnsig,weight1, weight2 = 5, 5, 0.7, 0.3, 6.4, 0.3
#
## Simulation params 
#RedNoiseL,RandomSeed,aliasTbin, tbin = 100,12,1,b
#
## create mixture model (gamma and lognorm)
#model = Mixture_Dist([st.gamma,st.lognorm],[3,3],[[[2],[0]],[[2],[0],]])
#
## load data lightcurve 
#datalc = Load_Lightcurve(route+datfile,tbin) 
#
## estimate underlying variance of data light curve 
#datalc.STD_Estimate() 
#
#
#X=np.arange (1.0, 3.2, 0.2) 
#Z=np.arange(0,1.2, 0.005 ) 
#
#for y in range (X.shape[0]): 
#    z=X[y] 
#    print z
#    for Y in range (Z.shape[0]): 
#        w=Z[Y] 
#        print w
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/HardXray/HardXray_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/' 
#        if not os.path.isdir(route1): 
#            os.makedirs(route1) 
#        A= w        
#        a_low=z 
#        a_high = z 
#
#        for j in range(1, 21): 
#            print j
#
#            # simulate LC with params above
#            delc = Simulate_DE_Lightcurve(datalc,BendingPL, \
#                    (A,v_bend,a_low,a_high,c),model, \
#                        (kappa,theta,lnmu,lnsig,weight1,weight2),size=1, \
#                        RedNoiseL=RedNoiseL,randomSeed=RandomSeed, \
#                            aliasTbin=aliasTbin, LClength=None)
#
#
#            # save lc
#            name='HardXraysim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(j))+'.dat'
#            delc.Save_Lightcurve(os.path.join(route1, name))

#u=86
## File Route
#route = "/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Used_Data/" 
#datfile = ('{}'.format(u))+'GHz.dat' 
#Da=np.loadtxt(route+datfile)
#sta=0
#sampling=[]
#for j in range (Da.shape[0]-1):
#    sta=Da[j+1,0]-Da[j,0]
#    sampling.append([sta])
#    sam=np.array(sampling)
#    b = int(sam.mean())
#
## PSD params
#v_bend=0.00345
#c=0 
#
## Probability density function params 
#kappa,theta,lnmu,lnsig,weight1, weight2 = 7.18, 5.268, 1.07214, 55.2866, -46.5508, 47.55084 
#
## Simulation params 
#RedNoiseL,RandomSeed,aliasTbin, tbin, LClength = 100,12,1,b, 200000
#
## create mixture model (gamma and lognorm)
#model = Mixture_Dist([st.gamma,st.lognorm],[3,3],[[[2],[0]],[[2],[0],]])
#
## load data lightcurve 
#datalc = Load_Lightcurve(route+datfile,tbin) 
#
## estimate underlying variance of data light curve 
#datalc.STD_Estimate() 
#
#X=np.arange (1.0, 3.1, 0.2) 
#Z=np.arange(0,1.2, 0.005 ) 
#
#for y in range (X.shape[0]): 
#    z=X[y] 
#    print z
#    for Y in range (Z.shape[0]): 
#        w=Z[Y] 
#        print w
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u))+'GHz/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/' 
#        if not os.path.isdir(route1): 
#            os.makedirs(route1) 
#        A= w        
#        a_low=z 
#        a_high = z 
#
#        for j in range(1, 2): 
#            print j
#
#            # simulate LC with params above
#            delc = Simulate_DE_Lightcurve(datalc,BendingPL, \
#                    (A,v_bend,a_low,a_high,c),model, \
#                        (kappa,theta,lnmu,lnsig,weight1,weight2),size=1, \
#                        RedNoiseL=RedNoiseL,randomSeed=RandomSeed, \
#                            aliasTbin=aliasTbin, LClength=LClength)
#
#
#            # save lc
#            name=('{}'.format(u))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(j))+'.dat'
#            delc.Save_Lightcurve(os.path.join(route1, name))
##            
##            
#u2=142
## File Route
#route = "/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Used_Data/" 
#datfile = ('{}'.format(u2))+'GHz.dat' 
#Da=np.loadtxt(route+datfile)
#sta=0
#sampling=[]
#for j in range (Da.shape[0]-1):
#    sta=Da[j+1,0]-Da[j,0]
#    sampling.append([sta])
#    sam=np.array(sampling)
#    b = int(sam.mean())
#
## PSD params
#v_bend=0.00345
#c=0 
#
## Probability density function params 
#kappa,theta,lnmu,lnsig,weight1, weight2 = 13.235, 2.879, -168.639, 1.139, 103.30135, 169.639
#
## Simulation params 
#RedNoiseL,RandomSeed,aliasTbin, tbin = 100,12,1,b
#
## create mixture model (gamma and lognorm)
#model = Mixture_Dist([st.gamma,st.lognorm],[3,3],[[[2],[0]],[[2],[0],]])
#
## load data lightcurve 
#datalc = Load_Lightcurve(route+datfile,tbin) 
#
## estimate underlying variance of data light curve 
#datalc.STD_Estimate() 
#
#
#X=np.arange (1.0, 3.1, 0.2) 
#Z=np.arange(0,1.2, 0.005 ) 
#
#for y in range (X.shape[0]): 
#    z=X[y] 
#    print z
#    for Y in range (Z.shape[0]): 
#        w=Z[Y] 
#        print w
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u2))+'GHz/'+('{}'.format(u2))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/' 
#        if not os.path.isdir(route1): 
#            os.makedirs(route1) 
#        A= w        
#        a_low=z 
#        a_high = z 
#
#        for j in range(1, 2): 
#            print j
#
#            # simulate LC with params above
#            delc = Simulate_DE_Lightcurve(datalc,BendingPL, \
#                    (A,v_bend,a_low,a_high,c),model, \
#                        (kappa,theta,lnmu,lnsig,weight1,weight2),size=1, \
#                        RedNoiseL=RedNoiseL,randomSeed=RandomSeed, \
#                            aliasTbin=aliasTbin, LClength=None)
#
#
#            # save lc
#            name=('{}'.format(u2))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(j))+'.dat'
#            delc.Save_Lightcurve(os.path.join(route1, name))
#            
            
#u2=230 
#
## File Route 
#route = "/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Used_Data/" 
#datfile = ('{}'.format(u2))+'GHz.dat' 
#
## PSD params
#v_bend=0.00345
#c=0 
#
## Probability density function params 
#kappa,theta,lnmu,lnsig,weight1, weight2 =6, 6, 0.8, 0.3, 7.4, 0.2 
#
## Simulation params 
#RedNoiseL,RandomSeed,aliasTbin, tbin, LClength = 100,12,1,8, 80000
#
## create mixture model (gamma and lognorm)
#model = Mixture_Dist([st.gamma,st.lognorm],[3,3],[[[2],[0]],[[2],[0],]])
#
## load data lightcurve 
#datalc = Load_Lightcurve(route+datfile,tbin) 
#
## estimate underlying variance of data light curve 
##datalc.STD_Estimate() 
#datalc.std=3.79650496199
#
#X=np.arange (1.0, 3.1, 0.2) 
#Z=np.arange(0,1.2, 0.005 ) 
#
#for y in range (X.shape[0]): 
#    z=X[y] 
#    print z
#    for Y in range (Z.shape[0]): 
#        w=Z[Y] 
#        print w
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u2))+'GHz/'+('{}'.format(u2))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/' 
#        if not os.path.isdir(route1): 
#            os.makedirs(route1) 
#        A= w        
#        a_low=z 
#        a_high = z 
#
#        for j in range(1, 2): 
#            print j
#
#            # simulate LC with params above
#            delc = Simulate_DE_Lightcurve(datalc,BendingPL, \
#                    (A,v_bend,a_low,a_high,c),model, \
#                        (kappa,theta,lnmu,lnsig,weight1,weight2),size=1, \
#                        RedNoiseL=RedNoiseL,randomSeed=RandomSeed, \
#                            aliasTbin=aliasTbin, LClength=LClength)
#
#
#            # save lc
#            name=('{}'.format(u2))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(j))+'.dat'
#            delc.Save_Lightcurve(os.path.join(route1, name))
#            
#u3=350
## File Route
#route = "/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Used_Data/" 
#datfile = ('{}'.format(u2))+'GHz.dat' 
#
## PSD params
#v_bend=0.00345
#c=0 
#
## Probability density function params 
#kappa,theta,lnmu,lnsig,weight1, weight2 = 7.18, 5.268, 1.07214, 55.2866, -46.5508, 47.55084 
#
## Simulation params 
#RedNoiseL,RandomSeed,aliasTbin, tbin, LClength = 100,12,1,8, 80000
#
## create mixture model (gamma and lognorm)
#model = Mixture_Dist([st.gamma,st.lognorm],[3,3],[[[2],[0]],[[2],[0],]])
#
## load data lightcurve 
#datalc = Load_Lightcurve(route+datfile,tbin) 
#
## estimate underlying variance of data light curve 
##datalc.STD_Estimate() 
#datalc.std=3.79650496199
#
#X=np.arange (1.0, 3.1, 0.2) 
#Z=np.arange(0,1.2, 0.005 ) 
#
#for y in range (X.shape[0]): 
#    z=X[y] 
#    print z
#    for Y in range (Z.shape[0]): 
#        w=Z[Y] 
#        print w
#        route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/'+('{}'.format(u2))+'GHz/'+('{}'.format(u2))+'GHz_'+('{}'.format(z))+'_A'+('{}'.format(w))+'/'
#        #route1='/media/chidiac/My Passport/DOCUMENTS/Masterarbeit/Power_Density_Spectrum/Simulated_PSD/' 
#        if not os.path.isdir(route1): 
#            os.makedirs(route1) 
#        A= w        
#        a_low=z 
#        a_high = z 
#
#        for j in range(1, 2): 
#            print j
#
#            # simulate LC with params above
#            delc = Simulate_DE_Lightcurve(datalc,BendingPL, \
#                    (A,v_bend,a_low,a_high,c),model, \
#                        (kappa,theta,lnmu,lnsig,weight1,weight2),size=1, \
#                        RedNoiseL=RedNoiseL,randomSeed=RandomSeed, \
#                            aliasTbin=aliasTbin, LClength=LClength)
#
#
#            # save lc
#            name=('{}'.format(u2))+'GHzsim_'+('{}'.format(z))+'_A'+('{}'.format(w))+'_'+('{}'.format(j))+'.dat'
#            delc.Save_Lightcurve(os.path.join(route1, name))
#
#
#
