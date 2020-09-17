
# Aula 04 A2 Atributos e Navegação

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

def find_by_href(browser, link):
    """Encontra o elemento 'a' com o link

    Args:
        browser: Instância do browser[Firefox, Chrome],
        link: Link a ser procurando em todas tags ancoras
    """
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento
        

browser = Firefox()
browser.get('http://selenium.dunossauro.live/aula_04_a.html')

elemento_ddg = find_by_text(browser, 'li', 'DuckDuckGo')

elemento_link_ddg = find_by_href(browser, 'ddg')



















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
        if text in elemento.text:
            return elemento    

def find_by_href(navegador, link):
    """Encontra o elemento <a></a> com o link
        Argumentos:
            browser = Instancia do browser [firefox, chrome,...]
            link = link que será procurado em todos os tags de ancora
    """
    elementos = navegador.find_elements_by_tag_name('a')
    
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

navegador = Firefox(executable_path='geckodriver.exe')
url = 'https://selenium.dunossauro.live/aula_04_a.html'
navegador.get(url)

# elemento_ddg = find_by_text(navegador, 'li', 'DuckDuckGo')
elemento_ddg = find_by_href(navegador, 'ddg') 
print(elemento_ddg.text)
print(elemento_ddg.get_attribute('href'))'''
