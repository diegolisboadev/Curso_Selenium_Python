
# Exercicio 07 Selenium com Python
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pprint import pprint

# TODO já verificando o label antes do click - agora tenho que os itens depois do click e popular o label
def preenche_form(wrapper, **values_inputs):
    wrapper.find_element_by_css_selector('label[id^="l"]').click()

    for i, val in values_inputs.items():
        wrapper.find_element_by_css_selector(f'input[name="{i}"]').send_keys(val)

    # wrapper.find_element_by_css_selector('input[name="btn"]').click()

    # clickLblBtnForm = wrapper.find_element_by_id('lbtn')
    # ActionChains(wrapper).move_to_element(clickLblBtnForm).click(clickLblBtnForm).perform()

    # clickBtnForm = wrapper.find_element_by_css_selector('input[id="btn"]')
    # ActionChains(wrapper).move_to_element(clickBtnForm).click(clickBtnForm).perform()



class Listener(AbstractEventListener):
    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'label':
            pprint(webdriver.find_element_by_id('lnome').text)
            pprint(webdriver.find_element_by_id('lemail').text)
            pprint(webdriver.find_element_by_id('lsenha').text)
    
    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            pprint(webdriver.find_element_by_id('lnome').text)
            pprint(webdriver.find_element_by_id('lemail').text)
            pprint(webdriver.find_element_by_id('lsenha').text)


browser = Firefox(executable_path='./geckodriver')

# Wrapper do WebDriver
wrapper = EventFiringWebDriver(browser, Listener())

wrapper.get('https://selenium.dunossauro.live/exercicio_07.html')

# Preencher o formulário
sleep(5)

dict_inputs = {
    'nome': 'Diego',
    'email': 'diego@uol.com',
    'senha': 'absksldc',
}
preenche_form(wrapper, **dict_inputs)