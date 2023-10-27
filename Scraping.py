import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()
driver.get("https://deirn.sdoe.com.br/diariooficialweb/#/home?diario=MTIx")


wait = WebDriverWait(driver,20)
edition_date = wait.until(EC.visibility_of_element_located((By.ID, 'dataEdicao')))
data_input = driver.find_element(By.ID,'dataEdicao')

initial_date = date(2023, 10, 25)
final_date = date(2023,10,25)

while initial_date <= final_date:
    formated_date = initial_date.strftime("%d/%m/%Y")
    time.sleep(2)
    edition_date.send_keys(formated_date)
    driver.implicitly_wait(5)

    ok_button = driver.find_element(By.ID, 'botaoNumeroEdicao')
    ok_button = wait.until(EC.presence_of_element_located((By.ID, 'botaoNumeroEdicao')))
    ok_button.click()
    time.sleep(5)
    impressa_button = wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Impressa")]')))
    impressa_button.click()
    download_button = wait.until(EC.presence_of_element_located((By.ID, 'download')))
    download_button.click()

    
    


