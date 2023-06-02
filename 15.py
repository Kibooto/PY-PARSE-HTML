import requests
from bs4 import BeautifulSoup

def get_body_descendants(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    body_tag = soup.find('body')
    
    if body_tag:
        descendants = body_tag.descendants
        print("Нащадки тегу <body>:")

        for descendant in descendants:
            if descendant.name:
                print(descendant.name)
    else:
        print("HTML-тег <body> не знайдено на веб-сторінці.")

url = "https://mof.gov.ua/uk"

get_body_descendants(url)
