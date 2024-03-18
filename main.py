from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import signal
import csv

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.nseindia.com/")
driver.maximize_window()

Market_Data_Hover = driver.find_element(By.ID, 'link_2')
Pre_Open_Market = driver.find_element(By.XPATH, '//*[@id="main_navbar"]/ul/li[3]/div/div[1]/div/div[1]/ul/li[1]/a')

actions = ActionChains(driver)

actions.move_to_element(Market_Data_Hover).move_to_element(Pre_Open_Market).click().perform()

driver.implicitly_wait(5)


countries = driver.find_elements(By.XPATH, '//table[@id="livePreTable"]/tbody/tr/td[2]/a')
prices = driver.find_elements(By.XPATH, '//table[@id="livePreTable"]/tbody/tr/td[7]')

FinalPrice = []

for i in range (50):
    tempo_data = {'Name': countries[i].text,
                  'Price': prices[i].text}
    FinalPrice.append(tempo_data)

df_data = pd.DataFrame(FinalPrice)
df_data

print(df_data)

df_data.to_csv('MyCSVFile.csv', index=False)

time.sleep(5)
driver.quit()
