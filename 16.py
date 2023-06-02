import requests
from bs4 import BeautifulSoup

def get_header_info(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    header = soup.find('h1')

    if header:
        header_html = str(header)
        header_text = header.get_text()
        parent_html = str(header.parent)

        print("HTML-код заголовка:")
        print(header_html)

        print("Текст заголовка:")
        print(header_text)

        print("HTML-код батьків заголовка:")
        print(parent_html)
    else:
        print("Заголовок не знайдено на веб-сторінці.")

url = "https://mof.gov.ua/uk"

get_header_info(url)
