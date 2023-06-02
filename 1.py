from bs4 import BeautifulSoup

def find_title(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    title_tag = soup.title
    if title_tag:
        return title_tag.text
    else:
        return None

filename = "test1.html"

try:
    with open(filename, 'r') as file:
        html_document = file.read()
        title = find_title(html_document)
        if title:
            print("Знайдений заголовок:", title)
        else:
            print("Заголовок не знайдений.")
except FileNotFoundError:
    print("Файл не знайдений.")
