from bs4 import BeautifulSoup

def get_first_h2_length(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    first_h2 = soup.find('h2')
    if first_h2:
        return len(first_h2.get_text())
    else:
        return 0
    
filename = "test5.html"

try:
    with open(filename, 'r') as file:
        html_document = file.read()
        first_h2_length = get_first_h2_length(html_document)
        print("Довжина тексту першого тегу <h2>: ", first_h2_length)
except FileNotFoundError:
    print("Файл не знайдений.")
