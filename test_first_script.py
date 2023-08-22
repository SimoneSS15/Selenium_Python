import time

from selenium import webdriver
browser = webdriver.Chrome()  # aqui está instanciando o chrome
browser.get("https://google.com")  # abre o google
time.sleep(5)
