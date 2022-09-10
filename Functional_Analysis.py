from sklearn import preprocessing
import numpy as np
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as alt
from scipy.stats import norm
import statistics
import random
from sklearn.metrics import r2_score
from statistics import mean
#p=997
#g=9.81
A=np.random.uniform(100000,1000000)

h=np.random.uniform(1,100) #Constant
#K=np.random.uniform(0.1,1) #Constant
#S=np.random.uniform(0,1)    #Constant

#r=1.99
sobs={}
robs={}
for joke in range (1) :
 K=np.random.uniform(0.1,1) 

 
 #RB=np.random.uniform(1,5000) #Varies

 #With Arranged Numbers

 L=np.arange(100,1000,0.1).tolist()
 t=30
 result2=[]
 drr=[]
 for i in L :
      
     a=i
     b=A*t*h*K
     Q=b/a
     Q=Q/1000000


     result2.append(Q)
 #print(result2)
 plt.plot(L,result2,label=K)
 
 robs[joke]=result2

 #Data Normalization
 result3=[result2]
 normalized = preprocessing.normalize(result3) #need to do this to normalize required data set
 #print("Normalized Data = ", normalized)

 # Plot between -10 and 10 with .001 steps.
 x_axis = normalized[0]
 sobs[joke]=x_axis


#Training Data Printer to show aggregate trainig curve 
 
L=np.arange(100,1000,0.1).tolist()
drr=[]
#for i in L :
 #drr.append((-0.000000032*i*i*i*i*i)+(0.0000117*i*i*i*i)-(0.1288*i*i*i)+(44.499*i*i)-(42715*i)+6234349)

#plt.plot(L,drr,label="training data") 







L=np.arange(100,1000,0.1).tolist() #Change this
si=[]
pi=[]
di=[]
ti=[]
mi=[]
ri=[]
gi=[]
for i in range (len(robs)) :
  j=[]
  myline=np.linspace(100,1000, 100) #change this it is to plot the predicte dline in some interval
  #mymodel = np.poly1d(np.polyfit(L,robs[i], 2))
  #plt.plot(myline, mymodel(myline),label='predicted 2')
  #mymodel = np.poly1d(np.polyfit(L,robs[i], 3))
  #plt.plot(myline, mymodel(myline),label='predicted 3')
  #mymodel = np.poly1d(np.polyfit(L,robs[i], 4))
  #plt.plot(myline, mymodel(myline),label='predicted 4')                  
  mymodel = np.poly1d(np.polyfit(L,robs[i], 5))
  #plt.plot(myline, mymodel(myline),label='predicted 5')
  j=(mymodel.coefficients)
  #print(mymodel)         #to show final modal 
  #print(mymodel(0))
  si.append(j[0])
  pi.append(j[1])
  di.append(j[2])
  ti.append(j[3])
  mi.append(j[4])
  gi.append(j[5])
  #print(r2_score(robs[i], mymodel(L)))
  ri.append(r2_score(robs[i],mymodel(L)))
  myline=np.linspace(100,1000, 100)
  #plt.plot(myline, mymodel(myline),label='predicted')
  
#print(si,pi,di,ri)
print('SI',mean(si),min(si), max(si))
print('PI',mean(pi),min(pi), max(pi))
print('DI',mean(di),min(di), max(di))
print('RI',mean(ri),min(ri), max(ri))
print(mean(ti),mean(mi),mean(gi))



plt.legend()
# naming the x axis
plt.xlabel('L')
# naming the y axis
plt.ylabel('Q')
  
# giving a title to my graph
plt.title('Functional Analysis with Varying Length for Equation Q=Ath/L')

# function to show the plot
plt.show()

for joke in range (len(sobs)) :
 x_axis=sobs[joke]   
 # Calculating mean and standard deviation
 mean = statistics.mean(x_axis)
 sd = statistics.stdev(x_axis)
  
 plt.plot(x_axis, norm.pdf(x_axis, mean, sd),label=joke)

#plt.legend()
plt.xlabel('Normalized Data Range ')
# naming the y axis
#plt.ylabel('Fre')
  
# giving a title to my graph
plt.title('Data Normalization')
plt.show()

