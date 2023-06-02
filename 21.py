import requests
from bs4 import BeautifulSoup

def find_nested_tags(url, parent_tags):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    nested_tags = soup.find_all(parent_tags)

    if nested_tags:
        print("Теги, що вкладені в", parent_tags, ":")
        for tag in nested_tags:
            print(tag)
    else:
        print("На веб-сторінці не знайдено тегів, що вкладені в", parent_tags)

url = "https://python.org/"
parent_tags = ["div", "p"]

find_nested_tags(url, parent_tags)
