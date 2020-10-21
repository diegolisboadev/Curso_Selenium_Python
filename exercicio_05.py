
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

url = "https://selenium.dunossauro.live/exercicio_05.html"
browser.get(url)

def preenche_forms(form, nome, senha):
    """Preenche os forms 4 dinamicamente 

    Args:
        form ([type]): [Nome do form a ser preenchido]
        text ([type]): [Texto a ser passado para o input]
    """
    browser.find_element_by_css_selector(f'.form-{form} input[name="nome"]').send_keys(nome)
    browser.find_element_by_css_selector(f'.form-{form} input[name="senha"]').send_keys(senha)
    browser.find_element_by_css_selector(f'.form-{form} input[name="{form}"]').click()


# Code
sleep(3)

# Preenche o primeiro formulário
preenche_forms('l0c0', 'diego', '123')

# Preenche o segundo formulário
preenche_forms('l0c1', 'lucio', '345')

# Preenche terceito formulário
preenche_forms('l1c0', 'mario', '678')

# Preenche quarto form
preenche_forms('l1c1', 'paula', '91011')