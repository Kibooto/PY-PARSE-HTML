from bs4 import BeautifulSoup

def find_paragraphs(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    paragraphs = soup.find_all('p')
    return paragraphs

filename = "test2.html"

try:
    with open(filename, 'r') as file:
        html_document = file.read()
        paragraphs = find_paragraphs(html_document)
        if paragraphs:
            print("Знайдені теги <p>:")
            for p in paragraphs:
                print(p)
        else:
            print("Теги <p> не знайдені.")
except FileNotFoundError:
    print("Файл не знайдений.")
