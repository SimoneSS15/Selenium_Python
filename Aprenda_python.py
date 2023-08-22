import time

from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys('Simone')
time.sleep(5)
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('wirus1@gmail.com')
time.sleep(5)
navegador.find_element('xpath','//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button/span/b').click()