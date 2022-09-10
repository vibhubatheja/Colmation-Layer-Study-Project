from sklearn import preprocessing
import numpy as np

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
for joke in range (3) :
 #if(joke%1000==0)   :
  #print(joke)
 K=np.random.uniform(0.1,1) 

 A=np.random.uniform(100000,1000000)

 h=np.random.uniform(1,100)
 
 
 #With Arranged Numbers

 L=np.arange(100,1000,0.1).tolist()
 t=30
 result2=[]
 drr=[]
 for i in L :
      
     a=i
     b=A*t*h*K
     Q=b/a


     result2.append(Q)
 #print(result2)
 plt.plot(L,result2,label=K)
 
 robs[joke]=result2

 #Data Normalization
## result3=[result2]
## normalized = preprocessing.normalize(result3) #need to do this to normalize required data set
 #print("Normalized Data = ", normalized)

 # Plot between -10 and 10 with .001 steps.
 ##x_axis = normalized[0]
 ##sobs[joke]=x_axis





#With Random Numbers








L=np.arange(100,1000,0.1).tolist() #Change this
L01=np.arange(100,1000,0.1)
si=[]
pi=[]
di=[]
ti=[]
mi=[]
ri=[]
gi=[]
a1=[]
b2=[]
for i in range (len(robs)) :
  #if(i%1000==0)   :
    
   #print(i)
  j=[]

  myline=np.linspace(100,1000, 100) #change this it is to plot the predicte dline in some interval
  #print(len(L),len(robs[i]))
  #mymodel = np.poly1d(np.polyfit(L,robs[i], 4))
  #plt.plot(myline, mymodel(myline),label='predicted 4')
  mymodel = np.polyfit(np.exp(1/L01), robs[i], 1)
  #mymodel = np.poly1d(np.polyfit(L,robs[i], 5))
  #plt.plot(myline, mymodel(myline),label='predicted 5')  ## Can use this to show training data set we are using 

  #print(mymodel)
  #print(type(mymodel))
  #print(mymodel[0],mymodel[1])
  j12=mymodel[0]
  j22=mymodel[1]
  a1.append(j12)
  b2.append(j22)
  mymodel2=[]
  
  
  
  #for iii in L :
    #jjj=(j12+j22*np.exp(1/iii))
    #jjj=-jjj
    #mymodel2.append(jjj)
  #plt.plot(L,mymodel2,label='test data regression')
  #print(len(robs[i]),len(mymodel2))

  #print('this is r2',r2_score(mymodel2,robs[i]))    
  #ri.append(r2_score(robs[i],mymodel2))
  #myline=np.linspace(100,1000, 100)
  #plt.plot(myline, mymodel(myline),label='predicted')

#print(a1,b2)
#print(min(a1),max(a1),min(b2),max(b2))
print(mean(a1),mean(b2))
a11=mean(a1)
b11=mean(b2)


#print(a1,b2)


#Training Data Printer
 
L=np.arange(100,1000,0.1).tolist()
drr=[]
for i in L :
 drr.append(-(453419477.4631397+-453416793.5175331*np.exp(1/i)))
plt.plot(L,drr,label="training data") 

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
#plt.show()

