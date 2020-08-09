#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
get_ipython().system('{sys.executable} -m pip install -U selenium')


# In[19]:


import zipfile
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://eportal.miteco.gob.es/BoleHWeb/')

string_year = 'select[name="year"] option[value="1"]'
desplegable_year = driver.find_element_by_css_selector(string_year)
click_desplegable_year = desplegable_year.click()

time.sleep(2)

string_month = 'select[name="month"] option[value="0"]'
desplegable_month = driver.find_element_by_css_selector(string_month)
click_desplegable_month = desplegable_month.click()

time.sleep(2)

string_day = '//button[@onclick="javaScript:montarFecha(31)"]'
desplegable_day = driver.find_element_by_xpath(string_day)
click_desplegable_day = desplegable_day.click()

time.sleep(2)

string_download = '//button[@id="btnMnuBoletinPDF"]'
desplegable_download = driver.find_element_by_xpath(string_download)
click_desplegable_download = desplegable_download.click()


# In[ ]:





# In[ ]:




