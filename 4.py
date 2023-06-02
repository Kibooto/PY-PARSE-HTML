from bs4 import BeautifulSoup

def get_first_paragraph_text(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    first_paragraph = soup.find('p')
    if first_paragraph:
        return first_paragraph.get_text()
    else:
        return None

filename = "test4.html"

try:
    with open(filename, 'r') as file:
        html_document = file.read()
        first_paragraph_text = get_first_paragraph_text(html_document)
        if first_paragraph_text:
            print("Текст першого тегу <p>:")
            print(first_paragraph_text)
        else:
            print("Тег <p> не знайдений.")
except FileNotFoundError:
    print("Файл не знайдений.")
