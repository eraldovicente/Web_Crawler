#!/usr/bin/env python
# coding: utf-8

# In[4]:


import urllib.request

fhand = urllib.request.urlopen('http://openwebinars.net/')
for line in fhand:
    print(line.decode().strip())


# In[5]:


# Análisis de HTML mediante BeautifulSoup


# In[8]:


# Instalación de la libreria
import sys
get_ipython().system('{sys.executable} -m pip install beautifulsoup4   ')


# In[14]:


import urllib
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://openwebinars.net/')
soup = BeautifulSoup(html)

tags = soup('a')

for tag in tags:
    print('TAG:', tag)
    print('URL', tag.get('href'))
    print('CONTENIDO', tag.contents)
    print('ATRIBUTO', tag.attrs)
    print('\n')


# In[12]:


tags


# In[ ]:




