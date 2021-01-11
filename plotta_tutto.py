#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


#mi serve per manipolare file
import os


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


#cartella nella quale voglio lavorare. Metterò dentro il caso che voglio analizzare.
#se tutto funziona bene è l'unica cosa che devo cambiare di volta in volta.
principale="plottatutto/"


# In[6]:



#c è la lista dei nomi dei file nella cartella corrente

cartelle=os.listdir(principale)
for i in range(len(cartelle)):                           #per tutte le cartelle 
    path=principale+cartelle[i]+"/postProcessing/turbineOutput/0/"
    file=os.listdir(path)

    for j in range(len(file)):                           # per tutti i files
    #ricorda che il + serve a concatenare le stringhe
        A=pd.read_csv(path+file[j],sep=' ',skiprows=1,header=None)
        B=A.values
        # -------------------------------------------------------------------------plotta grandezze
        if B.shape[1]<6:    # questo è per le grandezze globali tipo rotorTorque
            variable_te=B[:,-1]
            time=B[:,1]
        else:               # questo è per le grandezze locali tipo bladePointAlpha
            variable_te=B[0:-1:3,-20]
            variable_sw=B[-1,4:-1]
            span=np.linspace(0,63,len(variable_sw))
            time=B[0:-1:3,2]
            plt.figure()
            plt.plot(span,variable_sw)
            plt.title(file[j])
            plt.xlabel("radius")
            plt.ylabel(file[j])
            plt.savefig(principale+cartelle[i]+"/"+file[j]+"_sw.eps")
        plt.figure()
        plt.plot(time,variable_te)
        plt.title(file[j])
        plt.xlabel("time [s]")
        plt.ylabel(file[j])
        plt.savefig(principale+cartelle[i]+"/"+file[j]+"_te.eps")
      
       
         # ----------------------------------------------------------------------------------------
   


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




