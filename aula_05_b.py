
from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

browser = Firefox()

url = 'http://selenium.dunossauro.live/aula_05_b.html'
browser.get(url)

#
topioco = browser.find_element_by_class_name('topico').text
linguagens = browser.find_elements_by_class_name('linguagens')

for ling in linguagens:
    # pprint(ling.find_element_by_tag_name('h2').text)
    # pprint(ling.find_element_by_tag_name('p').text)
    pprint((ling.find_element_by_tag_name('h2').text, ling.find_element_by_tag_name('p').text))