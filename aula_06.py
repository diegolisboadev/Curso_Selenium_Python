
from selenium.webdriver import Firefox
from time import sleep

browser = Firefox()
url = "https://selenium.dunossauro.live/aula_06_a.html"
browser.get(url)

#
browser.find_element_by_css_selector('input').send_keys('Diego')
