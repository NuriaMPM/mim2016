# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:26:59 2016

@author: isa_uniovi
"""

import numpy as np
from numpy import linalg as alg
import matplotlib.pyplot as plt
from mlabwrap import mlab

a=array([[0, 1, 2],[2, 3, 4], [4, 5, 6] ])
[m,n]=shape(a)
mq=a[:,1]/alg.norm(a[:,1]);
mr=zeros([n,n]);
mr[1,1]=norm(a[:,1]);
for k in range(2,n):
   q=mq[:,1:k-1];
   q=eye(m)-mq*mq';
   mq(:,k)=q*a(:,k);
   mr(k,k)=norm(mq(:,k));
   mq(:,k)=mq(:,k)/mr(k,k);
   for j=1:k-1,
        mr(j,k)=mq(:,j)'*a(:,k);
   end 
end
