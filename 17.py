import requests
from bs4 import BeautifulSoup

def print_li_tags(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    li_tags = soup.find_all('li')

    if li_tags:
        print("Теги <li> на веб-сторінці:")
        for tag in li_tags:
            print(tag)
    else:
        print("Теги <li> не знайдено на веб-сторінці.")

url = "https://mof.gov.ua/uk"

print_li_tags(url)
