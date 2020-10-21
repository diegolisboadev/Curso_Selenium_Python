
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox(executable_path='./geckodriver')
browser.get("https://www.diariooficial.ma.gov.br")

#Code
# sleep(5)

# Fechar modal Alert
# modal_close = browser.find_element_by_css_selector('a[role=button]')
# modal_close.click()

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
input_data_ini.send_keys('01/10/2018')

input_data_fim = browser.find_element_by_xpath('//input[@name="formPesq:calendarFim_input"]')
input_data_fim.send_keys('19/10/2020')

# Set Input Campo Pesquisa
input_pesquisa = browser.find_element_by_xpath('//input[@name="formPesq:inputTerm"]')
input_pesquisa.send_keys('Segurança')

# Input Button Click
input_click = browser.find_element_by_xpath('//input[@name="formPesq:j_idt90"]').click()

sleep(5)

table = browser.find_element_by_xpath('//table[@role="grid"]')
tbody = table.find_elements_by_xpath("//table[@role='grid']//td[@role='gridcell']")
for t in tbody:
    t_attr = t.get_attribute('href')
    print(t_attr)
    # print(t.text)







