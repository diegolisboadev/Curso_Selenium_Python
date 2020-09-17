
# Exercicio 1 Selenium com Python (Dunossauro)

from selenium.webdriver import Firefox
from time import sleep

navegador = Firefox(executable_path='geckodriver.exe')

# Url
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

# Pegar o site
navegador.get(url)

# Tempo de espera
sleep(5)

# Pegar a TAG H1
h1 = navegador.find_element_by_tag_name('h1')

atributo = navegador.find_elements_by_tag_name('p')

lista = []
dicio = {}

# Lista a tag 'p'
for num in atributo:
    atributos = num.get_attribute('atributo')
    textos = num.text
    lista.append([atributos, textos])

print('=-'*50)
dicio[h1.tag_name] = dict(lista)
print(dicio)

navegador.quit()
