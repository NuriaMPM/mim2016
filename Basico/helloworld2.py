# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:41:44 2016

@author: isa_uniovi
"""

import numpy as np
import matplotlib.pyplot as plt

# Hola mundo !
print('Hola')

# Abrir archivo de datos
f1='../Datos/Xsens/Antebrazo50copia.txt';
fID1 = open(f1,'r');

data1 = np.loadtxt(fID1)
(numfilas,numcols)=data1.shape
print('Matriz con ' + str(numfilas) + ' filas y ' + str(numcols) + ' columnas.')

#Close the text file
fID1.close()

#---------------

#Cada columna de los datos anteriores corresponde a:
ax=1;ay=2;az=3;
gx=4;gy=5;gz=6;
mx=7;my=8;mz=9;
freq=100

#Empezamos trabajando solo con los datos estáticos:
start_in=1;
size_frame=200;

#%% Dividimos las 13 columnas de datos en 3 de accs y 3 de gyros
accx=data1[start_in:size_frame,ax]
accy=data1[start_in:size_frame,ay]
accz=data1[start_in:size_frame,az]
acc1=np.array([accx,accy,accz])

gyrx=data1[start_in:size_frame,gx]
gyry=data1[start_in:size_frame,gy]
gyrz=data1[start_in:size_frame,gz]
gyr1=np.array([gyrx,gyry,gyrz])

#%% plots varios
plt.figure()
plt.ion()
plt.plot(acc1.T)
plt.plot(gyr1.T)
plt.show()

#%% Media de las primeras aceleraciones
medias=np.mean(acc1, axis=1)  
print('Medias de acelerómetros:' + str(medias))

#%% Media de los primeros giros
medias=np.mean(gyr1, axis=1)  
print('Medias de giróscopos:' + str(medias))

#en el mac no va esto:
#raw_input("Press enter to finish...")

