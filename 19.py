import requests
from bs4 import BeautifulSoup

def print_elements_by_id(url, element_id):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all(id=element_id)

    if elements:
        print("Елементи з ідентифікатором '", element_id, "':")
        for element in elements:
            print(element)
    else:
        print("Елементи з ідентифікатором '", element_id, "' не знайдено на веб-сторінці.")

url = "https://python.org/"

element_id = "header"

print_elements_by_id(url, element_id)
