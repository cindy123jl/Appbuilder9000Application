import requests
from bs4 import BeautifulSoup

page = requests.get('http://books.toscrape.com/')

soup = BeautifulSoup(page.content, 'html.parser')

html_list = list(soup.children)

print(html_list)

element = [type(item) for item in list(soup.children)]

print(element)



