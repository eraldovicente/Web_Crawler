import random
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://www.olx.com.br/autos-e-pecas')