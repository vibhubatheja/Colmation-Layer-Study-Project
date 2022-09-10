

import csv
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from itertools import pairwise 

def goreader(abst,nummero) :
   #print(nummero+1)
   k=[]
   abst2=[abst]
   for i in abst2 :

       k=k+i.split()
   k=[abst]   

   counter4=collections.Counter(k)

   wa=''
   zo=[]
  
   for zo in k :
       if '.' in zo :
        zo=zo.strip('..')
       if '.' in zo :
        zo=zo.strip('.,')
       wa=wa+' '+zo
    
   k=[]
   k=wa.split()
       
   
   counter4=collections.Counter(k)

   
   duckduck=['the','of','to','The','a','in','and','for','that','by','is','with','are','on','was','as','from','by','were','be','an','at','this','which','have','using','can','This','. or','been','used','has','A','Than','.In']
 
   for i in duckduck :
       if i in counter4 :
           del(counter4[i])

   return(0)

    
def letsdoreading(aaa,bbb,nu) :
    
    flag='no'
    if 'colmation' in aaa :
     print(nu+1)
     flag='yes'
     print("in condition 1")
    if 'Colmation' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 2")
    if 'River Bed Filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 3")
    if 'River bed Filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 4")
    if 'river bed filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 5")
    if 'river Bed filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 6")
    if 'river bed Filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 6")
    if 'River Bed filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 7")
    if 'river Bed Filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 8")
    if 'Riverbed filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 9")
    if 'Riverbed Filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 10")
    if 'river Bed Filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 11")
    if 'riverbed filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 12")
    if 'river bed Filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 13")
    if 'river bed filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 14")
    
    if 'clogging' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 15")
    
    if 'Clogging' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 16")
    
    if 'River Bed Resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 17")
    
    if 'River bed resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 18")
    
    if 'river bed resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 19")
    
    if 'river Bed Resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 20")
    
    if 'river bed Resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 21")
    
    if 'River Bed Resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 22")
    
    if 'Riverbed Resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 23")
    
    if 'Riverbed resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 24")
    if 'Riverbed resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 25")
    if 'riverbed resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 26")
    if 'riverbed Resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 27")

    if 'bed resistance' in aaa :
        if flag=='no':
           print(nu+1)
           
           print("in condition 28")
           #if 'river' in aaa :
           flag='yes'   
            #print(nu+1,"IN CLASUE 28b")

    if 'Bed Resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 29")

    if 'bed Resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 30")

    if 'Bed resistance' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 31")

    if 'bed filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 32")

    if 'Bed filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 33")

    if 'Bed Filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 34")
    if 'bed Filtration' in aaa :
        if flag=='no':
           print(nu+1)
           flag='yes'
           print("in condition 35")
    if flag=='yes':
      #print(aaa)
      return(nu+1)
     
    if flag=='no':
     return(0)
    
    
           


with open('D:\SS 22\Study Project\Python Codes\Data Analysis\meth222.csv', 'r') as infile: # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]
abstra=data['Abstract']
counter=0
j=[]
for zo in abstra :
    counter=counter+1
    
    opp=goreader(zo,counter)
    opp2=letsdoreading(zo,opp,counter)
    if opp2>0 :
     j.append(opp2)
print("Paper Search Opration Completed")
print("Found",len(j),"relavent papers to the topic out of 200")
print("List of those papers is listed below")
print(j)
#print(len(j))
le='This is to find if in it actually works or it is just pretending to work'

