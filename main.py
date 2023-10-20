import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service ()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options = options)

url = 'https://deirn.sdoe.com.br/diariooficialweb/#/home?diario=MTIx'

driver.get(url)

input_elements = driver.find_elements(By.TAG_NAME, 'input')


for input_elements in input_elements: 
    print(input_elements.text)

driver.quit() 

