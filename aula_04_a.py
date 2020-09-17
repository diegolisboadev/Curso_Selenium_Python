
# Aula 04 A Atributos e Navegação

from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

url = 'http://selenium.dunossauro.live/aula_04_a.html'
browser.get(url)

sleep(5)

lista_n_ordenada = browser.find_element_by_tag_name('ul') # Pegar o 1 li
lis = lista_n_ordenada.find_elements_by_tag_name('li') # Pegar todos os lis do 1 ul
lis[0].text # Texto do 1 li do 1 ul
lis[0].find_element_by_tag_name('a').text # Pegar o texto da tag 'a' dentro da tag 'li'
href = lis[0].find_element_by_tag_name('a') # Pegar o atributo 'href' do navegador
href.get_attribute('href') # Pegar o atributo da tag 'a'























'''from selenium.webdriver import Firefox
from time import sleep

navegador = Firefox(executable_path='geckodriver.exe')
url = 'https://selenium.dunossauro.live/aula_04_a.html'
navegador.get(url)

lista_n_ordenada = navegador.find_element_by_tag_name('ul')
lis = navegador.find_elements_by_tag_name('li')

lis[0].text

lis[0] = navegador.find_element_by_tag_name('a').text'''


