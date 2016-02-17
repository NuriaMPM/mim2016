# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:35:10 2015

@author: dalvarez
"""
import math
import numpy as np
import matplotlib.pyplot as plot
from scipy import signal

def Codo_TRIAD(file1,file2,start_in):
#%%Función para el procesamienot de dos sensores y estimación de ángulos del
#codo


  # Open the text file.
  fileID1 = open(file1,'r');
  fileID2 = open(file2,'r');

  #%% Read columns of data according to format string.
  #%Supongo data1 es el antebrazo
  data1 = np.genfromtxt(fileID1,delimiter='\t',skip_header=5)
  data2 = np.genfromtxt(fileID2,delimiter='\t',skip_header=5)
  
  #Close the text file.
  fileID1.close()
  fileID2.close()

  ax=1;ay=2;az=3;
  gx=4;gy=5;gz=6;
  mx=7;my=8;mz=9;
  freq=100

  (numdatos,nada)=data1.shape

  #%%Calibramos el brazo y damos por bueno el antebrazo
  accx=data1[start_in:start_in+50,ax]
  accy=data1[start_in:start_in+50,ay]
  accz=data1[start_in:start_in+50,az]
  acc1=np.array([accx,accy,accz])
  magx=data1[start_in:start_in+50,gx]
  magy=data1[start_in:start_in+50,gy]
  magz=data1[start_in:start_in+50,gz]
  mag1=np.array([magx,magy,magz])
  accx=data2[start_in:start_in+50,ax]
  accy=data2[start_in:start_in+50,ay]
  accz=data2[start_in:start_in+50,az]
  acc2=np.array([accx,accy,accz]);
  magx=data2[start_in:start_in+50,gx]
  magy=data2[start_in:start_in+50,gy]
  magz=data2[start_in:start_in+50,gz]
  mag2=np.array([magx,magy,magz])

  acc1=np.mean(acc1,axis=1)
  mag1=np.mean(mag1,axis=1)
  acc2=np.mean(acc2,axis=1)
  mag2=np.mean(mag2,axis=1)

  #%%Base del sensor referencia (considerada correcta)
  V1ref=acc1/np.linalg.norm(acc1)
  tmp=mag1/np.linalg.norm(mag1)
  V2ref=np.cross(V1ref,tmp)
  V2ref=V2ref/np.linalg.norm(V2ref)
  V3ref=np.cross(V1ref,V2ref)
  Vref=np.transpose(np.array([V1ref,V2ref,V3ref]))

  #%%Base del sensor movil
  V1=acc2/np.linalg.norm(acc2)
  tmp=mag2/np.linalg.norm(mag2)
  V2=np.cross(V1,tmp)
  V2=V2/np.linalg.norm(V2)
  V3=np.cross(V1,V2)
  V=np.transpose(np.array([V1,V2,V3]))

  #%% Cálculo de la matriz de rotación
  R=np.matrix(Vref)*(np.matrix(V).getI())
  print R


  #%%Se desplazan las aceleraciones medidas en el antebrazo de acuerdo a la
  #%%%expresión del sólido rígido
  accx=data1[:,ax]
  accy=data1[:,ay]
  accz=data1[:,az]
  acc1=np.array([accx,accy,accz])
  wx=data1[:,gx]
  wy=data1[:,gy]
  wz=data1[:,gz]
  w1=np.array([wx,wy,wz])
  magx=data1[:,mx]
  magy=data1[:,my]
  magz=data1[:,mz]
  mag1=np.array([magx,magy,magz])
  alfax=np.concatenate([np.array([0]),np.diff(wx)])*freq
  alfay=np.concatenate([np.array([0]),np.diff(wy)])*freq
  alfaz=np.concatenate([np.array([0]),np.diff(wz)])*freq
  alfa=np.array([alfax,alfay,alfaz])
  r=np.array([0.14,0,0.02]) #distancias a los que se coloquen los sensores del
                              #punto de rotación
  for indice in range(0,numdatos):
    acc1[:,indice]=acc1[:,indice]-np.cross(alfa[:,indice],r)-np.cross(w1[:,indice],np.cross(w1[:,indice],r))

  #%%Se rotan todas las aceleraciones medidas en el brazo de acuerdo a la matriz
  #$$ de calibración calculada
  accx=data2[:,ax]
  accy=data2[:,ay]
  accz=data2[:,az]
  acc2=np.zeros((3,numdatos))
  for indice in range(0,numdatos):
    acc2[:,indice]=np.transpose(R*np.matrix([[accx[indice]],[accy[indice]],[accz[indice]]]))
  wx=data2[:,gx]
  wy=data2[:,gy]
  wz=data2[:,gz]
  w2=np.zeros((3,numdatos))
  for indice in range(0,numdatos):
    w2[:,indice]=np.transpose(R*np.matrix([[wx[indice]],[wy[indice]],[wz[indice]]]))
  magx=data2[:,mx]
  magy=data2[:,my]
  magz=data2[:,mz]
  mag2=np.zeros((3,numdatos))
  for indice in range(0,numdatos):
    mag2[:,indice]=np.transpose(R*np.matrix([[magx[indice]],[magy[indice]],[magz[indice]]]))

  #%%%Se desplazan las aceleraciones medidas en el brazo de acuerdo a la
  #%%expresión del sólido rígido
  alfax=np.concatenate([np.array([0]),np.diff(w2[0,:])])*freq; 
  alfay=np.concatenate([np.array([0]),np.diff(w2[1,:])])*freq;
  alfaz=np.concatenate([np.array([0]),np.diff(w2[2,:])])*freq;
  alfa=np.array([alfax,alfay,alfaz])
  r=np.array([-0.08,0,0.04])

  for indice in range(0,numdatos):
    acc2[:,indice]=acc2[:,indice]-np.cross(alfa[:,indice],r)-np.cross(w2[:,indice],np.cross(w2[:,indice],r))

  #%%Estimatición final de todso los ángulos
  flex=np.zeros(numdatos)
  pron=np.zeros(numdatos)
  for indice in range(0,numdatos):
    V1=acc1[:,indice]/np.linalg.norm(acc1[:,indice])
    tmp=mag1[:,indice]/np.linalg.norm(mag1[:,indice])
    V2=np.cross(V1,tmp)
    V2=V2/np.linalg.norm(V2)
    V3=np.cross(V1,V2)
    V=np.transpose(np.array([V1,V2,V3]))

    v1=acc2[:,indice]/np.linalg.norm(acc2[:,indice])
    tmp=mag2[:,indice]/np.linalg.norm(mag2[:,indice])
    v2=np.cross(v1,tmp)
    v2=v2/np.linalg.norm(v2)
    v3=np.cross(v1,v2)
    v=np.transpose(np.array([v1,v2,v3]))

    R=np.matrix(V)*(np.matrix(v).getI())

    flexion=math.atan(-R[0,2]/R[0,0])
    pronacion=math.atan(-R[2,1]/R[1,1])
    
    if (flexion<-0.75*math.pi/2):
        flexion=flexion+math.pi
        
    
    flex[indice]=flexion*180/math.pi;
    pron[indice]=-pronacion*180/math.pi;
  
  #%%Falta el filtro de butterworth.
  b,a=signal.butter(8,0.06)
  flex=signal.lfilter(b,a,flex)
  pron=signal.lfilter(b,a,pron)
  
  #plot.figure(1)
  #plot.subplot(211)
  plot.plot(flex)
  #plot.subplot(212)
  #plot.plot(pron)
  return (flex,pron)
  
if __name__ == '__main__':
    f1='Simple1.txt';
    f2='Simple2.txt';
    Codo_TRIAD(f1,f2,1000)
    