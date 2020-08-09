#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Extração de texto de um discurso

# instalación de la libreria pandas
import sys
get_ipython().system('{sys.executable} -m pip install pandas')


# In[23]:


import urllib
from bs4 import BeautifulSoup

url = 'https://brasil.elpais.com/brasil/2020-08-08/brasil-adoece-enquanto-bolsonaro-releva-a-pandemia-e-se-mantem-em-eterno-palanque-eleitoral.html'
html = urllib.request.urlopen(url)
soup2 = BeautifulSoup(html)

tags = soup2('p')
discurso = ''

for tag in tags:
        a = tag.contents[0]
        discurso = discurso + str(a)
        
contadores = dict()
discurso = discurso.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').lower()
palabras = discurso.split()

for palabra in palabras:
    if len(palabra)>3:
        contadores[palabra] = contadores.get(palabra, 0) + 1
        
import pandas
pandas.DataFrame(list(contadores.items()),columns=['palabra','contador']).sort_values('contador',ascending=False)


# In[ ]:




