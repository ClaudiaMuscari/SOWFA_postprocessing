#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os #mi serve per manipolare file
#----------------------------------------------------------------- sensitivity analysis caso con eps_ott
n_celle=[600000,1288832,6965235,50669856]   #non è importante il valore preciso, basta l'ordine di grandezza
#n_celle=[1.4, 2.8, 5.6, 11.2]


# In[16]:


dfdata = pd.read_csv('FAST/t1.T1.out', sep='\t', header=None, skiprows=10) #prendo direttamente output fast
datadata = dfdata.values


# In[17]:


#cartella nella quale voglio lavorare. Metterò dentro il caso che voglio analizzare.
#se tutto funziona bene è l'unica cosa che devo cambiare di volta in volta.
EVM="sensitivity/EVM/"
LOCAL="sensitivity/LOCAL/"
cartelleEVM=sorted(os.listdir(EVM))             # con sorted le metto in ordine numerico
cartelleLOCAL=sorted(os.listdir(LOCAL))
Torque_EVM=[0]*(len(cartelleEVM))
Torque_LOCAL=[0]*(len(cartelleLOCAL))
Torque_FAST=[(datadata[-1,6]*1000)]*(len(cartelleLOCAL))    
Thrust_EVM=[0]*(len(cartelleEVM))
Thrust_LOCAL=[0]*(len(cartelleLOCAL))
Thrust_FAST=[(datadata[-1,9]*1000)]*(len(cartelleLOCAL))






for i in range(len(cartelleLOCAL)):                           #per tutte le cartelle 
    path=EVM+cartelleEVM[i]+"/postProcessing/turbineOutput/0/"
    A=pd.read_csv(path+"rotorTorque",sep=' ',skiprows=1,header=None)
    B=A.values
    Torque_EVM[i]=B[-1,-1]   
    path=LOCAL+cartelleLOCAL[i]+"/postProcessing/turbineOutput/0/"
    A=pd.read_csv(path+"rotorTorque",sep=' ',skiprows=1,header=None)
    B=A.values
    Torque_LOCAL[i]=B[-1,-1]
    





for i in range(len(cartelleLOCAL)):                           #per tutte le cartelle 
    path=EVM+cartelleEVM[i]+"/postProcessing/turbineOutput/0/"
    
                      # per tutti i files
    #ricorda che il + serve a concatenare le stringhe
    A=pd.read_csv(path+"rotorAxialForce",sep=' ',skiprows=1,header=None)
    B=A.values
    Thrust_EVM[i]=B[-1,-1]
   
    path=LOCAL+cartelleLOCAL[i]+"/postProcessing/turbineOutput/0/"
        
    A=pd.read_csv(path+"rotorAxialForce",sep=' ',skiprows=1,header=None)
    B=A.values
    Thrust_LOCAL[i]=B[-1,-1]


            


# In[20]:


plt.figure()
plt.plot(n_celle,Torque_EVM, label="EVM")
plt.title("TORQUE")
plt.xlabel("n_celle")
plt.ylabel("Torque")

plt.plot(n_celle,Torque_FAST, label="FAST")

plt.plot(n_celle,Torque_LOCAL, label="LOCAL")
plt.legend()
plt.savefig("sensitivity"+"/TORQUE")


# In[21]:


plt.figure()
plt.plot(n_celle,Thrust_EVM, label="EVM")
plt.title("Thrust")
plt.xlabel("n_celle")
plt.ylabel("Thrust")

plt.plot(n_celle,Thrust_LOCAL, label="LOCAL")

plt.plot(n_celle,Thrust_FAST, label="FAST")
plt.legend()
plt.savefig("sensitivity"+"/THRUST")





