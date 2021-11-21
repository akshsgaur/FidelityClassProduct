from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
options = Options()
options.add_argument('--headless')
br = webdriver.Firefox(options=options)
url ="https://www.fidelity.ca/fidca/en/products/de?series=B"
soup = BeautifulSoup(br.page_source,'html.parser')
print(soup.find_all(class_ = 'item'))