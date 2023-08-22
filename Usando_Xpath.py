import time

from selenium import webdriver
from selenium.webdriver.common.by import By
navegador = webdriver.Chrome()
navegador.get("https://www.google.com")
#navegador.find_element(By.ID, "input").send_keys("Selenium python")
#Esse trecho do código não funciona
time.sleep(5)
