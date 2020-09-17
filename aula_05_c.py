
from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint
from urllib.parse import urlparse
from json import loads

browser = Firefox()

# url = 'http://selenium.dunossauro.live/aula_05_c.html'
url = 'http://selenium.dunossauro.live/aula_05.html'
browser.get(url)

def preenche_form(browser, nome, email, senha, telefone):
    """Preenche form com Selenium

    Args:
        browser ([type]): [instancia do browser]
        nome ([type]): [name input nome]
        email ([type]): [name input email]
        senha ([type]): [name inpu senha]
        telefone ([type]): [name input telefone]
    """
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()

#
sleep(3)
estrutura = {
    'nome': 'Diego', 
    'email': 'dilisboapires@uol.com', 
    'senha': 'er98932df', 
    'telefone': '989999898'
}

preenche_form(browser, **estrutura)

#
sleep(5)
url_parseada = urlparse(browser.current_url)
pprint(url_parseada)
url_parseada.query 
url_parseada.query.split()
browser.find_element_by_id('result')

text_resultado = browser.find_element_by_id('result').text
resultado_arrumado = text_resultado.replace('\'', "\"")  # Trocar asplas simples por duplas

dict_resultado = loads(resultado_arrumado)

assert dict_resultado == estrutura # Verificar se a expressão é verdadeira ou não

''''def melhor_filme(browser, filme, email, telefone):
    """Informa o melhor do filme, email e 
    telefone para form filme melhor

    Args:
        browser: ['instância do browser']
        filme: ['informa o nome do filme']
        email: ['informa o email']
        telefone: ['informa o telefone']
    """
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()

#
melhor_filme(browser, 'Parasita', 'dilisboapires@uol.com', '(098)9898-9898')'''

#
'''browser.find_element_by_name('filme')
browser.find_element_by_name('filme').send_keys('Pantera Negra')
browser.find_element_by_name('email').send_keys('dilisboapires@hotmail.com')
browser.find_element_by_name('telefone').send_keys('(098)9898-9898')
browser.find_element_by_name('enviar').click()'''
