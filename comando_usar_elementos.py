import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)  # aqui está instanciando o chrome
browser.get("https://www.saucedemo.com")  # abre o google
time.sleep(5)
