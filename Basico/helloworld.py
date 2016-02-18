# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:40:17 2016

@author: isa_uniovi
"""

import numpy as np


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