#Ejercicio de mínimos cuadrados
#Nuria María Pérez Mas

import numpy as np #Importar libreria de matrices
import matplotlib.pyplot as plt #Importar librería de dibujo de graficas
#p(0)=0, p(5)=0, p(10)=1
#v(0)=0, v(10)=0
#INPUT=Fuerza f
n=10

#Primero se construirá la matriz Ap  (p=Ap·f)
Ap=np.zeros((n,n),dtype=float) #crear matriz de ceros
Ap.fill(0.5) #llenarla de 0.5
Ap=np.tril(Ap,0) #quedarse sólo con la triangular lower

for i in range (n):
    for j in range (i):
        for k in range (j,i):
            Ap[i,j]=Ap[i,j]+1
#print (Ap) #ya tenemos la matriz Ap

#Se construirá ahora la matriz Av
Av=np.tril(np.ones((n, n), dtype=float), 0)
#print (Av) #ya tenemos la matriz Av

#Ahora se tienen que tener en cuenta sólo las restricciones:
#p(0) =0  = Ap[0,]  · f
#p(5) =0  = Ap[5,]  · f
#p(10)=1  = Ap[9,] · f
#v(0) =0  = Av[0,]  · f
#v(10)=0  = Av[9,] · f
# y       =   A     · f

y=np.array([0,0,1,0,0],dtype=float) #vector y con restricciones de posicion y velocidad
#A=([[Ap[0,:]],[Ap[5,:]],[Ap[9,:]],[Av[0,:]],[Av[9,:]]])
A=np.array([[0.5,0,0,0,0,0,0,0,0,0],[5.5,4.5,3.5,2.5,1.5,0.5,0,0,0,0],[9.5,8.5,7.5,6.5,5.5,4.5,3.5,2.5,1.5,0.5],[1,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1]])
#y=np.array([0,1,0],dtype=float) #vector y con restricciones de posicion y velocidad
#A=np.array([[5.5,4.5,3.5,2.5,1.5,0.5,0,0,0,0],[9.5,8.5,7.5,6.5,5.5,4.5,3.5,2.5,1.5,0.5],[1,1,1,1,1,1,1,1,1,1]])
#print (A)

Apinv=np.linalg.pinv(A) #obtener la pseudoinversa
#print (Apinv)

f=np.zeros((n,1),dtype=float) #vector de fuerzas

f=Apinv.dot(y)
#print (f)
#print (np.linalg.norm(f)) #Norma

#Obtención de vectores posición y velocidad
p=Ap.dot(f)
v=Av.dot(f)
print (p)
print (v)

#Gráficos
t = np.arange(0., 10., 1.) #vector de tiempo
plt.plot(t,p,'r--',t,v,'bs',t,f,'g^')

plt.show()