from bs4 import BeautifulSoup

def get_first_anchor_text(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    first_anchor = soup.find('a')
    if first_anchor:
        return first_anchor.get_text()
    else:
        return None

filename = "test6.html"

try:
    # Відкриття файлу
    with open(filename, 'r') as file:
        html_document = file.read()
        first_anchor_text = get_first_anchor_text(html_document)
        if first_anchor_text:
            print("Текст першого тегу <a>:")
            print(first_anchor_text)
        else:
            print("Тег <a> не знайдений.")
except FileNotFoundError:
    print("Файл не знайдений.")
