
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)

class Escuta(AbstractEventListener):
    def before_navigate_to(self, url, webdriver):
        print(f'Indo para {url}')

    def after_navigate_back(self, url):
        print('voltando para a página anterior...')

    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'Antes do click {elemento.tag_name}')

    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(webdriver.find_element_by_tag_name('span').text)
        print(f'depois do click {elemento.tag_name}')
        

browser = Firefox(executable_path="./geckodriver")

# Wrapper do WebDriver
rapidez = EventFiringWebDriver(browser, Escuta())

rapidez.get('https://selenium.dunossauro.live/aula_07_d.html')

input_texto = rapidez.find_element_by_tag_name('input')
span = rapidez.find_element_by_tag_name('span')
p = rapidez.find_element_by_tag_name('p')

input_texto.click()


rapidez.get('https://selenium.dunossauro.live/aula_07_c.html')
rapidez.back()




browser.quit()

