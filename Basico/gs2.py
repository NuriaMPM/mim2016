# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:26:59 2016

@author: isa_uniovi
"""

import numpy as np
from numpy import linalg as alg
import matplotlib.pyplot as plt



def gs2 (a):
    "factorizacion QR de la matriz a"
    [m,n]=np.shape(a)
    mq=np.zeros([m,n])
    mq[:,0]=a[:,0]/alg.norm(a[:,0])
    mr=np.zeros([n,n])
    mr[0,0]=alg.norm(a[:,0])

    for k in range(1,n):
        q=mq[:,0:k]                 # vector q anterior, extraido de Q
        q=np.eye(m)-(mq.dot(mq.T))
        mq[:,k]=q.dot(a[:,k])       # vector q~ perpendicular al a
        mr[k,k]=alg.norm(mq[:,k])   # rellenamos el coeficiente k,k de la R
        mq[:,k]=mq[:,k]/mr[k,k]     # vector q normalizado
        # El resto de columna de R son productos escalares de Q y A
        for j in range(0,k): 
            mr[j,k]=mq[:,j].T.dot(a[:,k])
    
    return (mq, mr)
   

am=np.array([[1, 2, 3],[2, 3, 4], [3, 4, 5]])
(mq,mr)=gs2(am)
print(mq.dot(mr))
