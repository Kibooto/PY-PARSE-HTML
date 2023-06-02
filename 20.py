import requests
from bs4 import BeautifulSoup

def find_first_tag_with_attribute_value(url, attribute, value):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    tag = soup.find(attrs={attribute: value})

    if tag:
        print("Перший тег з атрибутом '", attribute, "' та значенням '", value, "':")
        print(tag)
    else:
        print("Тег з атрибутом '", attribute, "' та значенням '", value, "' не знайдено на веб-сторінці.")

url = "https://python.org/"
attribute = "class"
value = "container"

find_first_tag_with_attribute_value(url, attribute, value)
