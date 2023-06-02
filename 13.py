import requests
from bs4 import BeautifulSoup

def print_html_tags(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    tags = soup.find_all()
    tag_names = set([tag.name for tag in tags])
    print("HTML-теги на веб-сторінці:")
    for tag_name in tag_names:
        print(tag_name)

url = "https://mof.gov.ua/uk"

print_html_tags(url)
