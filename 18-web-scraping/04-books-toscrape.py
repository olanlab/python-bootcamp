import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

from_pages = 1 
to_pages = 5

for page in range(from_pages, to_pages + 1):
    print("Scraping page : ", page)
    response = requests.get(f"{url}/catalogue/page-{page}.html")
    soup = BeautifulSoup(response.content, "html.parser")

    articles = soup.find_all("article", )

    for article in articles:
        title = article.select("h3 a")[0].get("title")
        price = article.find("p", class_="price_color").text.strip()
        print(title, price)
    
    print("================================================\n")