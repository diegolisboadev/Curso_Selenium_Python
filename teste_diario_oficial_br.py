
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.get("https://www.in.gov.br/leiturajornal")

# Code
# Seleciona Organização Principal
sleep(3)
slcOrgs = browser.find_element_by_css_selector('select[id=slcOrgs]')
slcOrgs.click()

# Seleciona MJ
mj = browser.find_element_by_xpath("//select/option[@value='Ministério da Justiça e Segurança Pública']")
mj.click()

# Busca o Diário
div_materias = browser.find_element_by_css_selector('div[id=hierarchy_content] .ul-materias')
li_materias = div_materias.find_elements_by_css_selector('.materia-link')

for li in li_materias:
    if 'Tribunal' in li.text:
        print(li.text)
