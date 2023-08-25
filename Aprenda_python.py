import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)  # aqui está instanciando o chrome

navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys('Simone')
time.sleep(5)
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('wirus1@gmail.com')
time.sleep(5)
navegador.find_element('xpath','//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button/span/b').click()

#Esse código abre uma página web com um curso de python, preenche os campos nome e e-mail e depois clica no botão principal da página