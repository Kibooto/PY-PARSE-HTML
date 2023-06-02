import requests
from bs4 import BeautifulSoup

def find_header_tags(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    header_tags_h1 = soup.find_all('h1')
    header_tags_h2 = soup.find_all('h2')
    header_tags_h3 = soup.find_all('h3')
    
    print("Теги <h1>:")
    for header_tag in header_tags_h1:
        print(header_tag.get_text())
    
    print("Теги <h2>:")
    for header_tag in header_tags_h2:
        print(header_tag.get_text())
    
    print("Теги <h3>:")
    for header_tag in header_tags_h3:
        print(header_tag.get_text())

url = "https://bank.gov.ua/"

print("Заголовки:")
find_header_tags(url)
