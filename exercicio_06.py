
from selenium.webdriver import Firefox
from time import sleep
import random

browser = Firefox(executable_path='./geckodriver')

url = "https://selenium.dunossauro.live/exercicio_06.html"
browser.get(url)


def preenche_forms(form, nome, senha):
    """Preenche 5 forms dinamicamente

    Args:
        form ([type]): [Nome do form a ser preenchido]
        nome ([type]): [Texto a ser passado para o input text nome]
        senha ([type]): [Texto a ser passado para o input senha password]
    """
    browser.find_element_by_css_selector(f'.form-{form} input[name="nome"]').send_keys(nome)
    browser.find_element_by_css_selector(f'.form-{form} input[name="senha"]').send_keys(senha)
    browser.find_element_by_css_selector(f'.form-{form} input[name="{form}"]').click()

def preenche_forms_randomico(form, nome, senha):
    """Preenche 5 forms dinamicamente
    Pegando o formulário que precisa preenche 
    e popular o form randomico setado

    Args:
        form ([type]): [Nome do form a ser preenchido]
        nome ([type]): [Texto a ser passado para o input text nome]
        senha ([type]): [Texto a ser passado para o input senha password]
    """
    browser.find_element_by_css_selector(f'.form-{form} input[name="nome"]').send_keys(nome)
    browser.find_element_by_css_selector(f'.form-{form} input[name="senha"]').send_keys(senha)
    browser.find_element_by_css_selector(f'.form-{form} input[name="{form}"]').click()

# Form 2
string_aleat_nome = 'abcdefghijklmnopqrstuvwyz'
string_aleat_senha = 'abcdefghijklmnopqrstuvwyz1234567890'
string_aleat_nome = ''.join(random.sample(string_aleat_nome,len(string_aleat_nome)))
string_aleat_senha = ''.join(random.sample(string_aleat_senha, len(string_aleat_senha)))

ativo = True
while(ativo):
    sleep(3)
    form_aleat_class = browser.find_element_by_css_selector('#grid header p > span').text

    if('... Mentira, você conseguiu terminar' not in form_aleat_class):
        preenche_forms_randomico(form_aleat_class, string_aleat_nome, string_aleat_senha)
    else:
        ativo = False

# Form 1
'''preenche_forms('l0c0', 'diego', '123')
preenche_forms('l0c1', 'lucio', '345')
preenche_forms('l1c0', 'mario', '678')
preenche_forms('l1c1', 'paula', '91011')
preenche_forms('l0c0', 'maria', 'asda23423')
preenche_forms('l0c0', 'liv', 'lkajsdkljas23333333e23')
preenche_forms('l0c0', 'uaysd', 'jedjekd867987')
preenche_forms('l0c0', 'hshs', 'oplaslqwd8787')'''
