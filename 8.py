import requests
from bs4 import BeautifulSoup

def get_li_urls(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    li_tags = soup.find_all('li')
    urls = []
    for li_tag in li_tags:
        anchor_tag = li_tag.find('a')
        if anchor_tag:
            href = anchor_tag.get('href')
            urls.append(href)
    return urls

url = "https://mof.gov.ua/uk"

li_urls = get_li_urls(url)
if li_urls:
    print("URL-адреси з тез <li>:")
    for li_url in li_urls:
        print(li_url)
else:
    print("URL-адреси не знайдено.")
