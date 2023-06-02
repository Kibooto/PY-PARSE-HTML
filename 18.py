import requests
from bs4 import BeautifulSoup

def print_element_content(url, search_string):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all(text=lambda text: search_string.lower() in text.lower())

    if elements:
        print("Елементи, що містять рядок '", search_string, "':")
        for element in elements:
            print(element.strip())
    else:
        print("Елементи, що містять рядок '", search_string, "' не знайдено на веб-сторінці.")

url = "https://bank.gov.ua/"

search_string = "Останні звіти"

print_element_content(url, search_string)
