
# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
data_set = pd.read_csv('practice.csv')
x = data_set.iloc[:,:].values

#calculating sum of each elements
N = np.sum(x, dtype = float)
z = x/N
 
#calculating columnmass and rowmass
columnmass = np.sum(z,axis = 0, dtype = float)
rowmass = np.sum(z, axis = 1, dtype = float)

columnmass = np.matrix(columnmass)
rowmass = np.matrix(rowmass)

#calculating rowprofile and columnprofile
rowprofile = z/np.transpose(rowmass)
columnprofile = z/columnmass

a = np.shape(x)
r = a[0]
c = a[1]

#Calculating weighted chi-squared distance
# D= Dr^(-0.5){z-RC'}Dc^(-0.5)


Dr = np.identity(r, dtype = float)
Dr = np.multiply(Dr,rowmass)

Dc = np.identity(c, dtype = float)
Dc = np.multiply(Dc, columnmass)

 #calculating inverse
Dri = np.linalg.inv(Dr)
Dci = np.linalg.inv(Dc)

Dri_sqrt = np.sqrt(Dri)
Dci_sqrt = np.sqrt(Dci)


A = z - np.dot(np.transpose(rowmass), columnmass)

D = np.dot(Dri_sqrt,A)
D= np.dot(D,Dci_sqrt)

#Calculating Singular value decomposition(svd)
U, S, Vt = np.linalg.svd(D)

V = np.transpose(Vt)




if c >= r:
    gr = c
    sm = r
else:
    gr = r
    sm = c
S1=np.zeros((gr,gr), dtype=float)
S2=np.zeros((sm,sm), dtype=float)
for i in range(gr):
    if i < sm:
        S1[i][i] = S[i]
for i in range(sm):
    if i < sm:
        S2[i][i] = S[i]

if r==sm:
    p = np.dot(Dri_sqrt, U)                             #calculating P
    P = np.dot(p,S2)                                   

    q = np.dot(Dci_sqrt,V)                              #calculating Q
    Q = np.dot(q,S1)
else:
    p = np.dot(Dri_sqrt, U)                             #calculating P
    P = np.dot(p,S1)

    q = np.dot(Dci_sqrt,V)                              #calculating Q
    Q = np.dot(q,S2)
    


