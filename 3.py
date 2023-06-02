from bs4 import BeautifulSoup

def count_paragraphs(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    paragraphs = soup.find_all('p')
    return len(paragraphs)

filename = "test3.html"

try:
    with open(filename, 'r') as file:
        html_document = file.read()
        count = count_paragraphs(html_document)
        print("Кількість тегів <p>: ", count)
except FileNotFoundError:
    print("Файл не знайдений.")
