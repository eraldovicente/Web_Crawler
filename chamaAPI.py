#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Open AQ Platform API

import urllib.request
import json

url1 = 'https://api.openaq.org/v1/cities'

pais = input('Introduzca las siglas del país (por ejemplo BR): ')

url2 = url1 + '?country=' + pais

datos = urllib.request.urlopen(url2).read().decode()

js = json.loads(datos)

for k in range(31):
    city = js['results'][k]['city']
    print(city)


# In[12]:


ciudad = input('Introduzca el nombre de una ciudad ')

url1 = 'https://api.openaq.org/v1/latest'

url2 = url1 + '?limit=1&city=' + ciudad

data = urllib.request.urlopen(url2).read().decode()

js = json.loads(data)
parameter = js['results'][0]['measurements'][0]['parameter']
valor = js['results'][0]['measurements'][0]['value']
unidades = js['results'][0]['measurements'][0]['unit']

print('El valor de ', parameter, 'en', ciudad, 'es de ', valor, unidades)


# In[ ]:




