from sklearn import preprocessing
import numpy as np
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as alt
from scipy.stats import norm
import statistics
import random

#g=9.81
A=np.random.uniform(10000,1000000)
#K=np.arange(0.1,1,0.1).tolist()
h=np.random.uniform(1,100) #Constant
L=np.random.uniform(1000,10000)
Q=np.random.uniform(100,1000)
t=30
K=np.arange(0.1,1,0.1).tolist()


#Case 1
result2=[]
dodo=[]
for i in K :
 a=np.random.uniform(1000,100000)
 dodo.append(a)
dodo.sort() 
for i in  range(len(K)) :
     j=K[i]
     a=dodo[i]
     
     Q=a*t*h*j/L
     result2.append(Q)
plt.plot(K,result2,label='A')

#Case2
result2=[]
dodo=[]
for i in K:
 h=np.random.uniform(1,100)
 dodo.append(h)
dodo.sort() 
for i in range((len(K))) :
     j=K[i]
     hi=dodo[i]
     Q=A*t*hi*j/L
     result2.append(Q)
plt.plot(K,result2,label='h')

#Case3
result2=[]
dodo=[]
for i in K:
 l=np.random.uniform(100,1000)
 dodo.append(l)
dodo.sort() 
for i in range((len(K))) :
     l=dodo[i]
     j=K[i]
     Q=A*t*h*i/l
     result2.append(Q)
#plt.plot(K,result2,label='L')

#Case3
result2=[]
dodo=[]
for i in K:
 to=np.random.uniform(0,30)
 dodo.append(to)
dodo.sort() 
for i in range((len(K))) :
     to=dodo[i]
     j=K[i]

     Q=A*j*h*to/L
     result2.append(Q)
plt.plot(K,result2,label='t')

  
plt.legend()
plt.show()
  












#plt.legend()
# naming the x axis
plt.xlabel('L')
# naming the y axis
plt.ylabel('Q')
  
# giving a title to my graph
plt.title('Functional Analysis with Varying Length and Discharge with constant K in each case')

# function to show the plot
plt.show()


