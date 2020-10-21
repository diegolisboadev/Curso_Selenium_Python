
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox(executable_path='geckodriver.exe')
browser.get('https://auxilio.caixa.gov.br/#/inicio')

# Acessar página de Acompanhamento da Solitação
sleep(5)
button_acom_solitacao = browser.find_element_by_class_name('secundario')
button_acom_solitacao.click() 

# Dados
cpf = '05976728308'
nome = 'Diego Lisboa Pires'
data_nasc = '22071994'
nome_mae = 'Rosidete Castro Lisboa'

sleep(3)
input_cpf = browser.find_element_by_id('mat-input-0').send_keys(cpf)
sleep(3)
input_nome = browser.find_element_by_id('mat-input-1').send_keys(nome)
sleep(3)
input_data_nasc = browser.find_element_by_id('mat-input-2').send_keys(data_nasc)
sleep(3)
input_nome_mae = browser.find_element_by_id('mat-input-3').send_keys(nome_mae)

# Click checkbox recaptcha
sleep(10)
checkbox_recaptcha = browser.find_element_by_xpath("//span[@id='recaptcha-anchor']").click()

# Click em Continuar
sleep(3)
button_continuar = browser.find_element_by_class_name('normal')
button_continuar.click()