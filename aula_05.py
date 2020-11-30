
from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

browser = Firefox(executable_path='./geckodriver')

url = 'http://selenium.dunossauro.live/aula_05_a.html'
browser.get(url)

# div1 = browser.find_element_by_tag_name('div')
div_py = browser.find_element_by_id('python')
div_hk = browser.find_element_by_id('haskell')
div_ls = browser.find_element_by_id('lisp')
h2 = div_py.find_element_by_tag_name('h2').text
pprint({'py': div_py.text, 'hk': div_hk.text, 'ls': div_ls.text})