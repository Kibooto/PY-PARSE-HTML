import requests
from bs4 import BeautifulSoup

def find_first_ten_links(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    link_tags = soup.find_all('a')
    count = 0
    for link_tag in link_tags:
        if count >= 10:
            break
        count += 1
        href = link_tag.get('href')
        print(href)
    
    print("Загальна кількість посилань:", len(link_tags))

url = "https://mof.gov.ua/uk"

print("Перші десять посилань:")
find_first_ten_links(url)
