
# Aula 04 B2 Atributos e Navegação (Location)

from selenium.webdriver import Firefox
from urllib.parse import urlparse
from pprint import pprint

browser = Firefox()
browser.get('https://selenium.dunossauro.live/aula_04_b.html')

url_parseada = urlparse(browser.current_url)








'''from selenium.webdriver import Firefox
from urllib.parse import urlparse

navegador = Firefox(executable_path='geckodriver.exe')
url = 'https://selenium.dunossauro.live/aula_04_b.html'
navegador.get(url)

url_parseada = urlparse(navegador.current_url)'''