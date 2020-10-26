
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
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
#th_span = table.find_element_by_css_selector('th[id="formPesq:tablePanelDados:j_idt102"] span[class="ui-column-title"]')
# tr_tag = table.find_elements_by_xpath("//div[@class='ui-datatable-tablewrapper']//table//tbody[@class='ui-datatable-data ui-widget-content']//tr")

# TODO Iterar de 8 em 8 para pegar somente o links com o TH fragmento
a_link = browser.find_elements_by_css_selector("td[role='gridcell'] a[href='#']")
for key, a in enumerate(a_link, 5):
    print(key)

'''if a_link[5].click():
    # return all handles value of open browser window 
    handles = browser.window_handles 
    for i in handles: 
        browser.switch_to.window(i)
        print(browser.title)'''

#ActionChains(browser).move_to_element(a).click(a).perform()
# a.click()









