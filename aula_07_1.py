
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    EventFiringWebDriver,
    AbstractEventListener
)
from time import sleep
from pprint import pprint

class Escuta(AbstractEventListener):
    def after_navigate_to(self, url, webdriver):
        print(f'indo para a url {url}')
    
    def after_navigate_back(self, webdriver):
        print('voltando...')
    """Pegar ação antes do click

    Args:
        AbstractEventListener ([type]): [description]
    """
    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            pprint(webdriver.find_element_by_tag_name('span').text)
        print("Antes do Click!!")

        """Pega ação depois do click no button
        """
    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            pprint(webdriver.find_element_by_tag_name('span').text)
        print("Depois do Click!!")

browser = Firefox()
rapi_browser = EventFiringWebDriver(browser, Escuta())
rapi_browser.get("https://selenium.dunossauro.live/aula_07_d.html")

# 
input_texto = rapi_browser.find_element_by_tag_name('input')
span = rapi_browser.find_element_by_tag_name('span')
p = rapi_browser.find_element_by_tag_name('p')

input_texto.click()
pprint("Estou clicando...")
assert "está com foco" == span.text, "não está em span"
pprint(span.text)
span.click()
assert "está sem foco" == span.text, "não está em span"
pprint(span.text)

#
assert p.text == "0", 'p não é zero'
input_texto.send_keys('batatinha')
span.click()
assert "está com foco" == span.text, "não está em span"
assert p.text == "1", 'p não é 1'

browser.quit
