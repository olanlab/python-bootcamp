import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(f"{url}")
soup = BeautifulSoup(response.content, "html.parser")

side_categories = soup.select("div.side_categories ul ul a")

for side_category in side_categories:
    
    category = side_category.text.strip()
    link = side_category["href"]
    print(f"{category} : {link}")