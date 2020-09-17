
# Exercicio 2 Selenium com Python (Dunossauro)

from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser.get(url)

sleep(5)

tag_h1 = browser.find_element_by_tag_name('h1').text
num_esperado = browser.find_elements_by_tag_name('p')[1].text

print(f'{tag_h1}')
print(f'{num_esperado}')

ancora = browser.find_element_by_id('ancora')
flag = True
while flag:
    ancora.click()
    tag_p = browser.find_elements_by_tag_name('p')
    for p in tag_p:
        if p.text != num_esperado and p.text != tag_p[0].text:
            num_esperado = ''.join(n for n in num_esperado if n.isdigit())
            num_sorteado = p.text[16:].strip()

            if f'Você ganhou: {num_esperado}' in p.text:
                print(f'Você Ganhou!!')
                flag = False
            elif num_esperado not in p.text:
                print(f'{p.text}')
                flag = True



'''from selenium.webdriver import Firefox
from time import sleep

navegador = Firefox(executable_path='geckodriver.exe')

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

navegador.get(url)

# Inicio da Resolução do problema
sleep(5)

text_h1 = navegador.find_element_by_tag_name('h1')
primeira_tag_p = navegador.find_elements_by_tag_name('p')[0] # Pegar a primeira tag <p></p>
segunda_tag_p = navegador.find_elements_by_tag_name('p')[1] # Pegar a segunda tag <p></p>

print('=-'*50)
print(f'{text_h1.text}\n')

num_esperado = segunda_tag_p.text[16:].strip()
print(segunda_tag_p.text) # Número Esperado:

# Usar While no Loop
tag_a = navegador.find_element_by_id('ancora')

while True:
    tag_a.click()
    tags_p = navegador.find_elements_by_tag_name('p')
    for k, p in enumerate(tags_p):
        valor_click = p.text[16:].strip()
        if f'Você ganhou: {valor_click}' in p.text:
            print(p.text)
            exit()
        elif p.text not in primeira_tag_p.text or p.text not in segunda_tag_p.text:
            print(f'{p.text}')
        # atributo_error = p.get_attribute('error')'''