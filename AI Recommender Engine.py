

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:00:34 2020

@author: Abhishek
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the Mentor Data
dataset1 = pd.read_csv('Mentor Data.csv')
X1 = dataset1.iloc[:,1:].values
#defining shape of matrix X1

a1=np.shape(X1)
row1=a1[0]
column2=a1[1]


# Importing the User Data
dataset2 = pd.read_csv('Aspirant Data.csv')
X2 = dataset2.iloc[:,1:].values

#defining shape of matrix X2
a2=np.shape(X2)
row2=a2[0]
column2=a2[1]


#defining minimum distance between mentor and user
dis=[]
id1=[]

#loop for calculating distance
for i in range(row2):
    mind=column2+1
    idd=0
    for j in range(row1):
        d=0
        #loop for numerical data
        for k in range(column2):
            if(k>4):
                if(k==5):
                    t=X1[j][k]-X2[i][k]
                    if(t<0):
                        t=t*(-1)
                    if(t>1):
                        d+=1*t       
                    else:
                        d+=0
                if(k==6):
                    t=X1[j][k]-X2[i][k]
                    if(t<0):
                        t=t*(-1)
                    if(t>10):
                        d+=0.3*(t/10)
                    else:
                        d+=0
                        
                if(k==7):
                    t=X1[j][k]-X2[i][k]
                   
                    if(t<0):
                        t=t*(-1)
                    if(t>10):
                        d+=0.1*(t/10)
                    else:
                        d+=0
            #loop for categorical Data
            elif(k==0):
                if(X1[j][k]!=X2[i][k]):
                    d+=5                     #sector is most important so
                                             #   weightage will be more                                 
            else:
                if(X1[j][k]!=X2[i][k]):
                    d+=1
            
        
        if(d<mind):
            mind=d
            idd=j
    
    dis.append(mind)
    id1.append(idd)
    
id1=np.array(id1)
x=pd.crosstab(index=id1,columns='count',dropna=True)
ll=[]              #defining a array for allocating mentor Id 
X11 = dataset1.iloc[:,:].values
for i in id1:
    ll.append(X11[i][0])
 
ll=np.array(ll)

#loop for calculating no. of user allotted to a mentor
numstudent = []
mentoridd = []
for i in range(row1):
    mentorid = X11[i][0]
    count = 0
    for jj in ll:
        if(jj==mentorid):
            count+=1
    numstudent.append(count)
    mentoridd.append(mentorid)
    

X22 = dataset2.iloc[:,:].values
M = ll
N = X22[:,0]

#plotting graph between user ID and mentor ID
plt.plot(M,N, 'ro')
plt.title("UserID Vs Mentor ID")
plt.xlabel("Mentor ID")
plt.ylabel("User ID")
plt.show()

#plotting graph between no. of user alloted and mentor ID
plt.plot(mentoridd, numstudent, 'ro')
plt.show()
#creating table with no. of user alloted and mentor ID
table=np.vstack((mentoridd, numstudent))
#creating table with user ID and Mentor ID
chart=np.vstack((M,N))
y=np.array(chart).astype(dtype=int)

    
            
                
