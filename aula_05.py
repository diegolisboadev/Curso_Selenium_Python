
from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

browser = Firefox()

url = 'http://selenium.dunossauro.live/aula_05_a.html'
browser.get(url)

# div1 = browser.find_element_by_tag_name('div')
div_py = browser.find_element_by_id('python')
div_hk = browser.find_element_by_id('haskell')
h2 = div_py.find_element_by_tag_name('h2').text
pprint(div_hk.text)