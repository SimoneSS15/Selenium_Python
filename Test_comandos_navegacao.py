
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)  # aqui está instanciando o chrome na variável browser (poderia ser outro nome)
# get()
browser.get("https://google.com")  # abre o google
time.sleep(5)

# maximize_window()
browser.maximize_window() # comando que irá maximizar a janela

# refresh()
browser.refresh() # funciona como o F5 na página, atualiza a mesma

# get()
browser.get("https://www.uol.com.br")
time.sleep(2)

# back()
browser.back()
# Esse comando volta para uma página anterior
time.sleep(2)

# forward()
browser.forward()
# Esse comando vai para a página a frente, nesse caso para a página do uol novamente
time.sleep(2)

# browser.switch_to.new_window("tab") # Esse comando vai abrir uma nova aba no navegador, para podermos usar
# # o comando close
# time.sleep(2)
# # close
# browser.close() # irá fechar a apenas a aba atual
# time.sleep(2)

browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(2)
# vai abrir mais duas abas para usarmos o comando close
# quit
browser.close()
# vai fechar tudo
