
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
browser.get("https://www.diariooficial.ma.gov.br/")

#Code
sleep(5)

# Fechar modal Alert
modal_close = browser.find_element_by_css_selector('a[role=button]')
modal_close.click()

# Pegar Div e do Select
sleep(5)
div_select = browser.find_element_by_css_selector('div .span10')

# Pegar Combo Select
select = div_select.find_element_by_xpath('//select[@id="formPesq:comboCaderno"]')
select.click()

option_combo = select.find_element_by_xpath('//option[@value="JU"]')
option_combo.click()

# Set data in input
input_data_ini = browser.find_element_by_xpath('//input[@name="formPesq:calendarInic_input"]')
input_data_ini.send_keys('01/01/2020')

input_data_fim = browser.find_element_by_xpath('//input[@name="formPesq:calendarFim_input"]')
input_data_fim.send_keys('16/09/2020')

# Set Input Campo Pesquisa
input_pesquisa = browser.find_element_by_xpath('//input[@name="formPesq:inputTerm"]')
input_pesquisa.send_keys('Lei 8.666/1993')

# Input Button Click
input_click = browser.find_element_by_xpath('//input[@name="formPesq:j_idt90"]')
input_click.click()






