from bs4 import BeautifulSoup

def get_first_anchor_href(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    first_anchor = soup.find('a')
    if first_anchor:
        return first_anchor.get('href')
    else:
        return None

filename = "test7.html"

try:
    with open(filename, 'r') as file:
        html_document = file.read()
        first_anchor_href = get_first_anchor_href(html_document)
        if first_anchor_href:
            print("Атрибут href першого тегу <a>:")
            print(first_anchor_href)
        else:
            print("Тег <a> не знайдений.")
except FileNotFoundError:
    print("Файл не знайдений.")
