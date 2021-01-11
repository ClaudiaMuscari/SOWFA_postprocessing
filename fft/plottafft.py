import numpy as np
from scipy.fft import fft, fftfreq
import pandas as pd
#mi serve per manipolare file
import os
import matplotlib.pyplot as plt
from scipy import signal



file="bladePointAlpha_loc3"
                  
 
#signal
A=pd.read_csv(file,sep=' ',skiprows=1,header=None)
B=A.values
time=B[7998:-1:3,2]     
y=B[7998:-1:3,40]

#sampling data
N =np.shape(y)[0]
dt=B[0,3]
SAMPLE_RATE=1/dt
DURATION=time[-1]-time[0]

#window
window = signal.hann(N)
y_win=y*window


#codice giacomo
df=1/(N*1/SAMPLE_RATE)

if N % 2 == 0:
    frequency=np.arange(0,N/2*df,df)
    specPos=frequency*2
    specTot=fft(y_win)
    specPos[0]=specTot[0]/N
    specPos[1:round(N/2)-1]=specTot[1:round(N/2)-1]/[N/2]
    specPos[round(N/2)-1]=specTot[round(N/2)]/N
else:
    frequency=np.arange(0,(N-1)/2*df,df)
    specPos=frequency*2
    specTot=fft(y_win)
    specPos[0]=specTot[0]/N
    specPos[1:round(N)/2]=specTot[1:round(N)/2]/(N/2)		

#plot
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(time,y)
plt.title(file)
plt.subplot(1,2,2)
plt.plot(frequency, abs(specPos))
plt.xlabel("frequency")
plt.ylabel("power")
plt.show()
       
       



