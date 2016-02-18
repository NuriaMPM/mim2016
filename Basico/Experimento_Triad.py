# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:15:33 2015

@author: dalvarez
"""

import Triad_Codo
import numpy as np

f1='../Datos/Xsens/Antebrazo50.txt';
f2='../Datos/Xsens/Brazo50.txt';
(flex,pron)=Triad_Codo.Codo_TRIAD(f1,f2,100)

salvar=np.matrix([flex,pron])
np.savetxt('../Resultados/TRIAD_50.txt',salvar.transpose())  

f1='../Datos/Xsens/Antebrazo150.txt';
f2='../Datos/Xsens/Brazo150.txt'
(flex,pron)=Triad_Codo.Codo_TRIAD(f1,f2,100)

salvar=np.matrix([flex,pron])
np.savetxt('../Resultados/TRIAD_150.txt',salvar.transpose())  

f1='../Datos/Xsens/Antebrazo300.txt';
f2='../Datos/Xsens/Brazo300.txt'
(flex,pron)=Triad_Codo.Codo_TRIAD(f1,f2,100)

salvar=np.matrix([flex,pron])
np.savetxt('../Resultados/TRIAD_300.txt',salvar.transpose())  
