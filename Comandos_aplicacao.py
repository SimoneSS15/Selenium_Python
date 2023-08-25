import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)  # aqui está instanciando o chrome
browser.get("https://www.saucedemo.com")

#title
print("O título da página é:", browser.title)
# vai printar no terminal o título da página do site saucedemo.com

#current_url
print("A URL da página é:", browser.current_url)

#page_source
print("O código fonte da página é :", browser.page_source)