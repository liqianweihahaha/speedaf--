from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:\Tools\chromedriver_win32\chromedriver.exe')
driver.get(
    "http://index.buffaloex.com/express/orderindex?projectType=customer&ticket=D4562BCF0A94E9E34AA3F37181F5B4EF")

txt = driver.find_element(By.XPATH, '//*[@id="receivepanel"]/div[1]/div[2]/div[3]/span/span[1]/span')
txt.click()
time.sleep(3)
txt = driver.find_element(By.XPATH, '//*[@id="select2-receivesuburb-results"]')
print(txt.text)