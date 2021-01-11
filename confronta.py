#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
#mi serve per manipolare file
import os
import matplotlib.pyplot as plt

#cartella nella quale voglio lavorare. Metterò dentro tutti i casi che voglio confrontare tra loro.
#se tutto funziona bene è l'unica cosa che devo cambiare di volta in volta.
principale="confronta"


dfdata = pd.read_csv('FAST/t1.T1.out', sep='\t', header=None, skiprows=10)
datadata = dfdata.values



#c è la lista dei nomi dei file nella cartella corrente

cartella=os.listdir(principale)
file=os.listdir(principale+"/"+cartella[0]+"/postProcessing/turbineOutput/0")
if os.path.exists(principale+"/"+cartella[0]+'/spanwise')==False:
    os.mkdir(principale+"/"+cartella[0]+'/spanwise')
    os.mkdir(principale+"/"+cartella[0]+'/time_evolution')
for j in range(len(file)):                           # per tutti i files
    #ricorda che il + serve a concatenare le stringhe
    path1=principale+"/"+cartella[0]+"/postProcessing/turbineOutput/0/" 
    path2=principale+"/"+cartella[1]+"/postProcessing/turbineOutput/0/"
    A1=pd.read_csv(path1+file[j],sep=' ',skiprows=1,header=None)
    A2=pd.read_csv(path2+file[j],sep=' ',skiprows=1,header=None)
    B1=A1.values
    B2=A2.values
        # -------------------------------------------------------------------------plotta grandezze
    if B1.shape[1]<6:    # questo è per le grandezze globali tipo rotorTorque
        variable1=B1[:,-1]
        variable2=B2[:,-1]
        time1=B1[:,1]
        time2=B2[:,1]
    else:               # questo è per le grandezze locali tipo bladePointAlpha
        variable1=B1[0:-1:3,-2]
        time1=B1[0:-1:3,2]
        variable2=B2[0:-1:3,-2]
        time2=B2[0:-1:3,2]
        variable1_sw=B1[-1,4:-1]
        variable2_sw=B2[-1,4:-1]
        span1=np.linspace(0,63,len(variable1_sw))
        span2=np.linspace(0,63,len(variable2_sw))
        span3=np.linspace(0,63,9)
        plt.figure()
     
        plt.plot(span1,variable1_sw,label=cartella[0])
     #   plt.hold(True)
        plt.plot(span2,variable2_sw,label=cartella[1])
        
        if file[j]=='bladePointAlpha':
            plt.plot(span3, datadata[-1,15:24], 'b', label = 'FAST')
        #if file[j]=='bladePointVaxial':
        #    plt.plot(span3, 8+datadata[-1,42:51], 'b', label = 'FAST')    
        if file[j]=='bladePointCd':
            plt.plot(span3, datadata[-1,96:105], 'b', label = 'FAST')   
        if file[j]=='bladePointCl':
            plt.plot(span3, datadata[-1,69:78], 'b', label = 'FAST')   
        if file[j]=='bladePointLift':
            plt.plot(span3, datadata[-1,123:132], 'b', label = 'FAST') 
        if file[j]=='bladePointDrag':
            plt.plot(span3, datadata[-1,151:160], 'b', label = 'FAST')       
        
        plt.title(file[j])
        plt.xlabel("radius")
        plt.ylabel(file[j])
        plt.legend()
        plt.savefig(principale+"/"+cartella[0]+"/"+"spanwise/"+file[j]+"_sw.eps")
    plt.figure()  
    plt.plot(time1,variable1,label=cartella[0])
    plt.plot(time2,variable2,label=cartella[1])
    
    if file[j]=='bladePointAlpha':
    	plt.plot(datadata[:,0], datadata[:,24], 'b', label = 'FAST')
    
  
    #if file[j]=='bladePointVaxial':
    #	plt.plot(datadata[:,0],datadata[:,51], 'b', label = 'FAST')    
    if file[j]=='bladePointCd':
        plt.plot(datadata[:,0], datadata[:,105], 'b', label = 'FAST')   
    if file[j]=='bladePointCl':
        plt.plot(datadata[:,0], datadata[:,78], 'b', label = 'FAST')   
    if file[j]=='bladePointLift':
        plt.plot(datadata[:,0], datadata[:,132], 'b', label = 'FAST') 
    if file[j]=='bladePointDrag':
        plt.plot(datadata[:,0], datadata[:,159], 'b', label = 'FAST')       
    if file[j]=='rotorTorque':
        plt.plot(datadata[:,0], datadata[:,6]*1000, 'b', label = 'FAST')
    if file[j]=='rotorPower':
        plt.plot(datadata[:,0], datadata[:,8]*1000, 'b', label = 'FAST')
    if file[j]=='rotorAxialForce':
        plt.plot(datadata[:,0], datadata[:,9]*1000, 'b', label = 'FAST')  
       
    
    plt.title(file[j])
    plt.xlabel("time [s]")
    plt.ylabel(file[j])
    plt.legend()
    plt.savefig(principale+"/"+cartella[0]+"/"+"time_evolution/"+file[j]+"_te.eps")
    #plt.show()
    







