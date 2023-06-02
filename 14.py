import requests
from bs4 import BeautifulSoup

def get_nested_tags(url, html_tag):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    parent_tag = soup.find(html_tag)
    
    if parent_tag:
        nested_tags = parent_tag.find_all()
        tag_names = set([tag.name for tag in nested_tags])
        print("Теги, вкладені в <", html_tag, ">:")
        for tag_name in tag_names:
            print(tag_name)
    else:
        print("HTML-тег <", html_tag, "> не знайдено на веб-сторінці.")

url = "https://mof.gov.ua/uk"
html_tag = "html"

get_nested_tags(url, html_tag)
