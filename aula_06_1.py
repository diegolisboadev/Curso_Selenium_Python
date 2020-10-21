
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

url = 'https://selenium.dunossauro.live/aula_06_a.html'
browser.get(url)

# find_element_by_css_selector por type [attr = valor]
#nome = browser.find_element_by_css_selector('[type="text"]')
#senha = browser.find_element_by_css_selector('[type="password"]')
#button = browser.find_element_by_css_selector('[type="submit"]')

# find_element_by_css_selector por name [attr = valor]
#nome = browser.find_element_by_css_selector('[name="nome"]')
#senha = browser.find_element_by_css_selector('[name="senha"]')
#button = browser.find_element_by_css_selector('[name="l0c0"]')

# find_element_by_css_selector por name [attr *= valor]
#nome = browser.find_element_by_css_selector('[name *= "ome"]')
#senha = browser.find_element_by_css_selector('[name *= "nha"]')
#button = browser.find_element_by_css_selector('[name *= "l0"]')

# find_element_by_css_selector por name [attr |= valor]
#nome = browser.find_element_by_css_selector('[name |= "nome"]')
#senha = browser.find_element_by_css_selector('[name |= "senha"]')
#button = browser.find_element_by_css_selector('[name |= "l0c0"]')

# find_element_by_css_selector por name [attr ^= valor]
nome = browser.find_element_by_css_selector('[name ^= "n"]')
senha = browser.find_element_by_css_selector('[name ^= "s"]')
button = browser.find_element_by_css_selector('[name ^= "l"]')

# Enviar Dados
nome.send_keys('Diego')
senha.send_keys('abc123')
button.click()

# Selector Universal
# browser.find_element_by_css_selector('*')

# Selector combinados
# browser.find_elements_by_css_selector('input[type$="t"]')
# browser.find_elements_by_css_selector('*[for *= "n"]')

#Selector por lista
#browser.find_elements_by_css_selector('label, input')

# Selector Irmãos adjacentes
# browser.find_elements_by_css_selector('div + br')
# browser.find_elements_by_css_selector('h2 + div')

# Selector geral adjacente
# browser.find_elements_by_css_selector('h2 ~ br')

# Selector filhos
# browser.find_elements_by_css_selector('div > br')

# Selector descendentes
# browser.find_elements_by_css_selector('form br')


