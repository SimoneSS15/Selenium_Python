import time

from selenium import webdriver
browser = webdriver.Chrome()  # aqui está instanciando o chrome
browser.get("https://www.saucedemo.com")

#title
print("O título da página é:", browser.title)
# vai printar no terminal o título da página do site saucedemo.com

#current_url
print("A URL da página é:", browser.current_url)

#page_source
print("O código fonte da página é :", browser.page_source)