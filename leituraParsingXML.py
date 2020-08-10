#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Lectura y parsing de XML

# Ler o arquivo XML de https://www.w3schools.com/xml/cd_catalog.xml e parsealo con a biblioteca ElementTree

import urllib.request
import xml.etree.ElementTree as ET

url = 'https://www.w3schools.com/xml/cd_catalog.xml'

data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data.decode())

lst = tree.findall('CD')

print('Número de CDs en el catálogo', len(lst))

for item in lst:
    print('\r')
    print('Titulo:', item.find('TITLE').text)
    print('Artista:', item.find('ARTIST').text)
    print('Precio:', item.find('PRICE').text)


# In[ ]:





# In[ ]:




