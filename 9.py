import requests
from bs4 import BeautifulSoup

def find_first_four_h2_tags(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    h2_tags = soup.find_all('h2')
    count = 0
    for h2_tag in h2_tags:
        if count >= 4:
            break
        count += 1
        print(h2_tag.get_text())

url = "https://bank.gov.ua/"

print("Перші чотири теги <h2>:")
find_first_four_h2_tags(url)
