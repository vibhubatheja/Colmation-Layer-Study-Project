import csv
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from itertools import pairwise 
from geopy.geocoders import Nominatim
import plotly.express as px
import pandas as pd
import numpy as np


def locplotdatamet(zoe) :
 geolocator = Nominatim(user_agent = "geoapiExercises")
 #del(zoe['Kathlenburg-Lindau'])
 ri={}
 print(zoe)
 for i in zoe :
  #print(i)   
  flag='do'  
  if i =='Olszytn'  :
    flag='up'
  if i=='Albany' :
    flag=='up'
  
  if flag=='do'  :
   location = geolocator.geocode(i)
   #print("Country Name: ", location)
   loc_dict=location.raw
   j=(loc_dict['display_name'].rsplit(',' , 1)[1])
   print(i,j)

   if j in ri :
      ri[j]=ri[j]+zoe[i]
   
   if j not in ri :
       ri[j]=zoe[i]
 print(ri)
 # Need to Edit Ri Source Output to get New Graph 
 
 np.random.seed(12)
 gapminder = px.data.gapminder().query("year==2007")
 #gapminder['counts'] = np.nan


 #d={'United Kingdom': 12, 'United States': 30, 'netherlands': 16, 'Germany': 8, 'switzerland': 3, 'Sri Lanka': 1, 'Malaysia': 1, 'China': 5, 'Poland': 1, 'Australia': 1, 'Slovakia': 1, 'Pakistan': 1, 'Romania': 1, 'Vietnam': 1, 'Canada': 2, 'Spain': 1}
 #d={'Romania': 3, 'Vietnam': 2, 'Pakistan': 1, 'United States': 46, 'Netherlands': 42, 'United Kingdom': 22, 'China': 10, 'Germany': 9, 'Switzerland': 5, 'Slovakia': 1, 'Australia': 1, ' Poland': 2, 'Malaysia': 1, 'Sri Lanka': 1, 'Spain': 1, 'Italy': 1, 'Madagascar': 1, 'Canada': 3}
 d={'India' :1000}
 for i in d :
    d[i]=[d[i]]
 print(d)    
 yourdata = pd.DataFrame(d).T.reset_index()
 yourdata.columns=['country', 'count']

 df=pd.merge(gapminder, yourdata, how='left', on='country')

 fig = px.choropleth(df, locations="iso_alpha",
                    color="count", 
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)

 fig.show()  

 
def getdataplotyrwise(counter) :
 yrco={}
 for i in range (1900,2022) :
   i=str(i)
   if i in counter :
     #print('a')
     yrco[i]=counter[i]

 
 timeinte={}
 counter2=yrco

 for i in range (1993,2022,5) :
     
   dokey=str(i+1)+'-'+str(i+5)
   
   sumkey=counter[(str(i+5))]+counter[(str(i+1))]+counter[(str(i+2))]+counter[(str(i+3))]+counter[(str(i+4))]
   timeinte[dokey]=sumkey
 
 return(timeinte)

def namepublic(counter) :
    jab={}
    for i in counter :
        if counter[i]>3 :
         jab[i]=counter[i]
    return(jab)

def wedonamethiagain(counter) :
    jab={}
    for i in counter :
        if counter[i]>40 :
         jab[i]=counter[i]
    return(jab)

def supercut(counter2,kl,rh,oi) :

 si=counter2.keys() 
 pi=counter2.values()
 fig = plt.figure()
 ax = fig.add_subplot(111)
 si=list(si)
 pi=list(pi)
 langs =si
 students = pi
 ax.bar(langs,students)
 plt.style.use('ggplot')
 plt.title(oi)
 plt.ylabel(kl)
 plt.tight_layout()
 plt.xlabel(rh)
 plt.show()
 
def supercutter(counter2,kl,rh,oi) :

 
 si=counter2.keys() 
 pi=counter2.values()
 si=list(si)
 pi=list(pi)
 yaxis = si
 xaxis = pi
 fig = plt.figure()
 ax = fig.add_subplot(111)
 ax.barh(yaxis,xaxis)
 plt.title(oi)
 plt.ylabel(kl)
 plt.xlabel(rh)
 plt.tight_layout()
 plt.show()

def abstracut(abst) :
   k=[]
   for i in abst :

       k=k+i.split()
       
   #need to remove full stops from words before counter processing
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

   
   duckduck=['during','study','is','into','but','water','the','of','to','The','a','in','and','for','that','by','is','with','are','on','was','as','from','by','were','be','an','at','this','which','have','using','can','This','or','been','used','has','A','Than','In','it']
   #crosschecklist 
   for i in duckduck :
       if i in counter4 :
           del(counter4[i])
   #print(counter4)       
   return(counter4)
def cloudywordday(counter) :
    #print(counter)
    word_could_dict=counter #plot lefy
    wordcloud = WordCloud(width = 1000, height = 500,background_color="red").generate_from_frequencies(word_could_dict)
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud,interpolation='bilinear')
    
def extratime(data) :
 things = {'Place': [], 'Publisher': [], 'WOS': []}
 
 for sentence in data:
     for k, v in pairwise(map(str.strip, sentence.split(':'))):
        for cat in things:
            if k.endswith(cat):
                for suffix in things:
                    v = v.removesuffix(suffix).strip()
                things[cat].append(v)
                break

 #print(things)
 return(things)

def letstravel(a,b) :
    
    a=a['Place']
    c=a+b
    c = list(filter(None,c))
    return(c)

            
def litcat(li) :
    jab={}
    for i in li :
        if li[i]>0 :
         jab[i]=li[i]
         
    return(jab)


    

# open the file in universal line ending mode 
with open('D:\SS 22\Study Project\Python Codes\Data Analysis\mathmaybe1.csv', 'r') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]
pubyr= data['PublicationYear'] #Need to Modify this shiot in Excel
pubti= data['PublicationTitle']
abstra=data['Abstract']
extrainn=data['Extra']
libcat=data['LibraryCatalog']
placecat=data['Place']



extradatadict=extratime(extrainn)  #do later for place sorting funnymade 
placeswego=letstravel(extradatadict,placecat)
publis=extradatadict['Publisher']


# Counters
counter9=collections.Counter(publis)
counter8=collections.Counter(placeswego)
counter4=abstracut(abstra)
counter=collections.Counter(pubyr)
counter3=collections.Counter(pubti)
counter6=collections.Counter(libcat)



#Data Set Selectors
intedata=getdataplotyrwise(counter)# to sort yearly 
dintedadta=namepublic(counter3)# to get more then 3+ results in Journals Published 
absdata=wedonamethiagain(counter4)# to get only 100+ results
lee=namepublic(counter6)   #for online lib 0+ 
plee=litcat(counter8)   #Places 0+
publee=namepublic(counter9)
plee={}
#print(plee)
locplotdatamet(plee)  # Used to Plot Graph of Loactions we want

#cloudywordday(counter3)
#print(absdata)
#cloudywordday(counter4)
#cloudywordday(counter4)
#Printers
#cloudywordday(publee)
#cloudywordday(counter)
#
#cloudywordday(lee)
#cloudywordday(plee)

#cloudywordday(counter9)
#cloudywordday(counter4) #can do absdata for 50+

#supercut(publee,'Year Published in', 'Frequency', 'Publisher for Papers')
#supercut(plee,'City Name','No of Repetations','Frequesncy')
#supercut(intedata,'Year Published in', 'Frequency', 'Papers per Year')

#supercutter(absdata,'Word','No of Repetations','Abstract Analysis')
#supercutter(lee,'Library Name','Frequency','Papers per Library')


 #can do absdata for 50+



