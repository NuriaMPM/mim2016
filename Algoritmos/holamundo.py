# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:47:03 2016

@author: juan
"""


import math
import numpy as np
import matplotlib.pyplot as plot
from scipy import signal

print('Hola')
f1='../Datos/Xsens/Antebrazo50copia.txt';
fID1 = open(f1,'r');

data1 = np.loadtxt(fID1)

#Close the text file.
fID1.close()

ax=1;ay=2;az=3;
gx=4;gy=5;gz=6;
mx=7;my=8;mz=9;
freq=100

(numdatos,nada)=data1.shape

start_in=1;
size_frame=1000;

#%%Calibramos el brazo y damos por bueno el antebrazo
accx=data1[start_in:size_frame,ax]
accy=data1[start_in:size_frame,ay]
accz=data1[start_in:size_frame,az]
acc1=np.array([accx,accy,accz])
magx=data1[start_in:size_frame,gx]
magy=data1[start_in:size_frame,gy]
magz=data1[start_in:size_frame,gz]
mag1=np.array([magx,magy,magz])
  
plot.plot(acc1)
  