
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()

url = "https://selenium.dunossauro.live/exercicio_06.html"
browser.get(url)

# Code TODO ver
def preenche_forms(form, nome, senha):
    """Preenche 5 forms dinamicamente

    Args:
        form ([type]): [Nome do form a ser preenchido]
        text ([type]): [Texto a ser passado para o input]
    """
    browser.find_element_by_css_selector(f'.form-{form} input[name="nome"]').send_keys(nome)
    browser.find_element_by_css_selector(f'.form-{form} input[name="senha"]').send_keys(senha)
    browser.find_element_by_css_selector(f'.form-{form} input[name="{form}"]').click()


# Form 1
preenche_forms('l0c0', 'diego', '123')
preenche_forms('l0c1', 'lucio', '345')
preenche_forms('l1c0', 'mario', '678')
preenche_forms('l1c1', 'paula', '91011')
preenche_forms('l0c0', 'maria', 'asda23423')
preenche_forms('l0c0', 'liv', 'lkajsdkljas23333333e23')
preenche_forms('l0c0', 'uaysd', 'jedjekd867987')
preenche_forms('l0c0', 'hshs', 'oplaslqwd8787')
