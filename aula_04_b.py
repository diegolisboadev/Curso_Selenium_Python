
# Aula 04 B Atributos e Navegação

from selenium.webdriver import Firefox
from time import sleep

def find_by_text(browser, tag, text):
    """
       Encontrar o elemento com texto 'text'

    Args:
        browser: Instância do browser [Firefox, chrome],
        text: [conteudo que deve está na tag],
        tag: Onde o texto será procurado
    """
    elementos = browser.find_elements_by_tag_name(tag) # lista
    for elemento in elementos:
        if elemento.text in text:
            return elemento

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_b.html')

textos = ['um', 'dois', 'tres', 'quatro']

for t in textos:
    find_by_text(browser, 'div', t).click()

for t in textos:
    sleep(2)
    browser.back()

for t in textos:
    sleep(2)
    browser.forward()



















'''from selenium.webdriver import Firefox
from time import sleep

def find_by_text(navegador, tag, text):
    """Encontrar o elemento com o texto `text`
       Argumentos:
        - navegador = Instancia do browser [firefox, chrome,...]
        - text = conteudo que deve está na tag
        - tag = tag onde o texto será procurado
    """
    elementos = navegador.find_elements_by_tag_name(tag)
    
    for elemento in elementos:
        if elemento.text == text:
            return elemento

navegador = Firefox(executable_path='geckodriver.exe')
url = 'https://selenium.dunossauro.live/aula_04_b.html'
navegador.get(url)

# elemento = find_by_text(navegador, 'div', 'um').click()

nome_das_caixas = ['um', 'dois', 'tres', 'quatro']
for texto in nome_das_caixas:
    find_by_text(navegador, 'div', texto).click()

# Voltar
for texto in nome_das_caixas:
    sleep(0.3)
    navegador.back()
for b in range(4):
    sleep(2)
    navegador.back()

# Pra frente novamente
for texto in nome_das_caixas:
    sleep(0.3)
    navegador.forward()'''