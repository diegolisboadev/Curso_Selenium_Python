
# Exercicio 05
from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from pprint import pprint
from json import loads

browser = Firefox()

url = 'https://selenium.dunossauro.live/exercicio_04.html'
browser.get(url)

def preenche_form(browser, nome, email, senha, telefone):
    """Preenche o form do exercicio 05

    Args:
        browser ([type]): [Intancia do browser]
        nome ([type]): [Nome]
        email ([type]): [email]
        senha ([type]): [senha]
        telefone ([type]): [telefone]
    """
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)

    browser.find_element_by_name('btn').click()

def url_parseada(browser):
    """Pegar a url resultado atual e parsear

    Args:
        browser ([type]): [instância do browser]
    """
    url_parseada = urlparse(browser.current_url)
    query_array = url_parseada.query.split()
    return query_array

def get_result_text_and_valida(browser, estrutura):
    """Pegar o resultado do texto e validar com assert

    Args:
        browser ([type]): [Instancia do browser]
        estrutura ([type]): [Dicionário da estrutura input]
    """
    main = browser.find_element_by_tag_name('main')
    result = main.find_element_by_tag_name('textarea').text
    result_org = result.replace('\'', "\"")
    result_org = result_org.replace('+', ' ')
    dict_result_url = loads(result_org)
    assert dict_result_url == estrutura

# Init Script
estrutura = {
    'email': 'dilisboapires@hotmail.com',
    'nome': 'Diego Lisboa',
    'senha': 'ahb9s7d9s',
    'telefone': '9899121312'
}

# 1 PARTE
sleep(5)
preenche_form(browser, **estrutura) # Usando dict como argumento (porém tem usar **kwargs)

# 2 PARTE
sleep(5)
query_array = url_parseada(browser)
get_result_text_and_valida(browser, estrutura)