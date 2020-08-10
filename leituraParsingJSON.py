#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Lectura y parsing de JSON

import json
f = open("presidents.json", "r")
info = json.loads(f.read())

print('Número de presidentes', len(info))

for item in info:
    print('\r')
    print('Nombre: ', item['president'])
    print('Partido: ', item['party'])


# In[ ]:





# In[ ]:




