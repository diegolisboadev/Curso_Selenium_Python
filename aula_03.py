
# Usando Selenium e Firefox
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox(executable_path='geckodriver.exe')

url = 'https://curso-python-selenium.netlify.app/aula_03.html'
# url = 'https://www.facebook.com/'

# Chamando uma Página
# browser.get('https://ddg.gg')
browser.get(url)

# Navegador encontre a TAG (a) do HTML
sleep(5)
# tag_a = browser.find_element_by_tag_name('a')
atributo_id = browser.find_element_by_id('ancora')
# tag_button = browser.find_element_by_id('u_0_13')

# Click na Tag (a)
# tag_a.click()
# atributo_id.click()
# tag_button.click()

# Retornar somente a 1 primeira ocorrência do elemento encontrado
# tag_p = browser.find_element_by_tag_name('p')

for click in range(10):
    # Retornar uma lista com todas as ocorrências da TAG
    tag_p = browser.find_elements_by_tag_name('p')
    atributo_id.click()
    print(f'Valor de p {tag_p[-1].text} valor do click: {click}')
    print(f'Os valores são iguais {int(tag_p[-1].text) == click}')
    # print(f'texto de p: {tag_p.text}')

# print(f'texto de a: {atributo_id.text}')
# print(f'texto de p: {tag_p.text}')

# Fecha o Browser
browser.quit()

