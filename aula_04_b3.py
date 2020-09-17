
# Aula 04 B2 Atributos e Navegação
"""
    1 - Pegar todos os links de Aulas;
        {'nome_aula': 'link_aula'}
    2 - Navegar até o exercicio 3;
            achar url do exercicio 3 e ir até lá
"""

from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

browser = Firefox()
browser.get('https://selenium.dunossauro.live/aula_04.html')

def get_links(browser, elemento):
    """ Pega todos os link dentro de um elemento
        Args:
            browser: Instância do navegador,
            elemento: webelement ['aside', 'main', 'body', 'ul', 'ol']
    """
    resultado = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')

    for ancora in ancoras:
        resultado[ancora.text] = ancora.get_attribute('href')

    return resultado



""" Parte 1 """

sleep(3)

pprint(get_links(browser, 'aside'))

'''aside = browser.find_element_by_tag_name('aside')
aside_ancoras = aside.find_elements_by_tag_name('a')
resultado_1 = {}
for ancora in aside_ancoras:
    resultado_1[ancora.text] = ancora.get_attribute('href')
pprint(resultado_1)'''

# browser.get(resultado_1['Aula 3']) // Acessar url em dict python

""" Parte 2 """

exercicio_3 = get_links(browser, 'main')
browser.get(exercicio_3['Exercício 3'])
















'''from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

navegador = Firefox(executable_path='geckodriver.exe')
url = 'https://selenium.dunossauro.live/aula_04.html'
navegador.get(url)

def get_links(navegador, elemento):
    """Pegar todos os links dentro de um elemento
        - navegador = Instancia do navegador
        - elemento = webelement[aside, main, body, ul, ol,...]
    """
    resultado = {}
    element = navegador.find_element_by_tag_name(elemento)
    a_tags = element.find_elements_by_tag_name('a')

    for ancora in a_tags:
        resultado[ancora.text] = ancora.get_attribute('href')

    return resultado


"""Parte 1"""
sleep(3)
pprint(get_links(navegador, 'aside'))

"""
navegador.get(resultado_1['Aula 3'])
navegador.get(resultado_1['Aula 4'])
"""

"""Parte 2"""
exercicio_3 = get_links(navegador, 'main')
pprint(exercicio_3)
navegador.get(exercicio_3['Exercício 3'])'''

