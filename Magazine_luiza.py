import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)  # aqui está instanciando o chrome

navegador.get("https://www.magazineluiza.com.br/")
