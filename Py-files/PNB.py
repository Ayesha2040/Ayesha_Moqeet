#!/usr/bin/env python
# coding: utf-8

# In[79]:


import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


#In the Audio file used there are sounds of different birds at different intervals. Each interval corresponding to a specfic bird has been trimmed and visualized 


# In[121]:


samplingFrequency, signalData = wavfile.read('pak_birds.wav')
signalData = signalData[:,0]


def plotspectogram(t1,t2,name):
    first = signalData[int(samplingFrequency*t1):int(samplingFrequency*t2)]
    fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,5))
    
    fig.suptitle(name,fontweight= 'heavy', size=15)
    ax1.plot(first)
    ax2.specgram(first,Fs=samplingFrequency)
    
    ax1.set_xlabel('Sample')
    ax1.set_ylabel('Amplitude')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Frequency')
    
    plt.show()


# In[122]:


plotspectogram(165,227,'Koel')


# In[124]:


plotspectogram(230,282,'BulBul')


# In[125]:


plotspectogram(290,348,'Lapwing')


# In[132]:


def plotspectogram_2(t1,t2,name):
    first = signalData[int(samplingFrequency*t1):int(samplingFrequency*t2)]
    fig, (ax1, ax2) = plt.subplots(2,1, figsize = (15,5))
    
    fig.suptitle(name,fontweight= 'heavy', size=15)
    ax1.plot(first)
    ax2.specgram(first,Fs=samplingFrequency)
    
    ax1.set_xlabel('Sample')
    ax1.set_ylabel('Amplitude')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Frequency')
    
    plt.show()
plotspectogram_2(165,348,'All three birds')

