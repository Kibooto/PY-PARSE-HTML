import requests
from bs4 import BeautifulSoup

def extract_text_from_webpage(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    webpage_text = soup.get_text()
    return webpage_text

url = "https://mof.gov.ua/uk"

webpage_text = extract_text_from_webpage(url)
print("Текст з веб-сторінки:")
print(webpage_text)
