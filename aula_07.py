
from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

browser = Firefox()
browser.get("https://selenium.dunossauro.live/aula_07_d.html")

input_texto = browser.find_element_by_tag_name('input')
span = browser.find_element_by_tag_name('span')
p = browser.find_element_by_tag_name('p')

input_texto.click()
assert "está com foco" == span.text, "não está em span"
pprint(span.text)
span.click()
assert "está sem foco" == span.text, "não está em span"
pprint(span.text)

#
assert p.text == "0", 'p não é zero'
input_texto.send_keys('batatinha')
span.click()
assert "está com foco" == span.text, "não está em span"
assert p.text == "1", 'p não é 1'

browser.quit