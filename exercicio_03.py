
# Exercicio 3 Selenium com Python (Dunossauro)

from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse
from pprint import pprint
from selenium.common import exceptions

def get_path(browser):
    """Pegar a página do current_url

    Args:
        browser: Instância do navegador
        page: Página (current_url)
    """
    pagina = urlparse(browser.current_url)
    return pagina.path

def click_result_value(browser, opcao = None):
    """Clicar tag 'a' do resultado

    Args:
        browser: Instância do navegador
    """
    main = browser.find_element_by_tag_name('main')
    if opcao in ['certo', 'errado']:
        main.find_element_by_xpath(f"//a[@attr='{opcao}']").click()
    elif opcao == None:
        sleep(2)
        a_click = main.find_elements_by_tag_name('a')
        if a_click[0].text == 'page_3.html':
            a_click[0].click()
    if opcao == '':
        sleep(2)
        tag_refresh = main.find_element_by_tag_name('p')
        if tag_refresh:
            browser.refresh()

browser = Firefox()
browser.get('https://selenium.dunossauro.live/exercicio_03.html')

sleep(5)
main = browser.find_element_by_tag_name('main')
ancora = main.find_element_by_tag_name('a').click()

sleep(10)
opcao = 'certo'
while True:
    path = get_path(browser)
    if path == '/page_1.html':
        click_result_value(browser, opcao)
    if path == '/diabao.html':
        browser.back()
        opcao = 'errado'
    if path == '/page_2.html':
        try:
            click_result_value(browser, 'certo')
        except exceptions.NoSuchElementException:
            browser.refresh()
            sleep(20)
    if path == '/page_3.html':
        click_result_value(browser, None)
    if path == '/page_4.html':
        click_result_value(browser, '')
        pprint('Sou o unicórnio da salvação! E você ganhou esse jogo!')
        break