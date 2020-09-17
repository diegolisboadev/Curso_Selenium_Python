
from selenium.webdriver import Firefox

browser = Firefox()

url = "https://selenium.dunossauro.live/aula_06_a.html"
browser.get(url)

# Code
browser.find_elements_by_css_selector('div.form-group')
browser.find_element_by_css_selector('div.form-group + br') # Selector Ajacente
browser.find_element_by_css_selector('div.form-group > br') # Selector Filho
len(browser.find_elements_by_css_selector('div + br')) # Quant de brs adjacentes de div encontrados 
browser.find_elements_by_css_selector('h2 ~ div') # Todo mundo que é geral adjacente div (iniciando em h2)
browser.find_elements_by_css_selector('form div') # Todas as divs que são descendentes do form