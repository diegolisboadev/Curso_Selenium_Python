
# Exercicio 07 Selenium com Python
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

# TODO pegar o click durante o click e/ou preenchimento do input
def preenche_form(wrapper, **values_inputs):

    for i, val in values_inputs.items():
        wrapper.find_element_by_id(f'l{i}').click()
        wrapper.find_element_by_name(f'{i}').send_keys(val)
        # wrapper.find_element_by_name(f'{i}').click()
    
    sleep(5)
    # wrapper.find_element_by_xpath('//input[@id=btn]').click()
    #button = wrapper.find_element_by_id('btn')
    #ActionChains(wrapper).move_to_element(button).click(button).perform()


class Listener(AbstractEventListener):
    def before_click(self, elemento, webdriver):
        print(f'Antes Click {elemento.text}')
    
    def after_click(self, elemento, webdriver):
        print(f'Depois do Click {elemento.text}')
        if elemento.tag_name == 'input':
            print('Mudança Input ' + webdriver.find_element_by_xpath('//label[@id="lnome"]').text)
            print('Mudança Input ' + webdriver.find_element_by_xpath('//label[@id="lemail"]').text)
            print('Mudança Input ' + webdriver.find_element_by_xpath('//label[@id="lsenha"]').text)
        
    '''def before_change_value_of(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print('Mudança Input ' + webdriver.find_element_by_xpath('//label[@id="lnome"]').text)
            print('Mudança Input ' + webdriver.find_element_by_xpath('//label[@id="lemail"]').text)
            print('Mudança Input ' + webdriver.find_element_by_xpath('//label[@id="lsenha"]').text)'''


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