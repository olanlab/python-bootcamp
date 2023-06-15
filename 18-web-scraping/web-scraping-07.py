import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"

response = requests.get(f"{url}")
soup = BeautifulSoup(response.content, "html.parser")

side_categories = soup.select("div.side_categories ul ul a")


with open("books.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["title", "category", "price", "href"])

    for side_category in side_categories:
        category = side_category.text.strip()
        link = side_category["href"].replace("index.html", "")
        print(f"{category} : {link}")
        print("===============================================================")
        
        from_pages = 1 
        to_pages = 5
        for page in range(from_pages, to_pages + 1):
            page_link = f"index.html" if page == 1 else f"page-{page}.html"
            
            book_list = requests.get(f"{url}{link}{page_link}")
            book_list_soup = BeautifulSoup(book_list.content, "html.parser")

            articles = book_list_soup.find_all("article", )
            if(len(articles) == 0):
                break

            for article in articles:
                title = article.select("h3 a")[0].get("title")
                href =  article.select("h3 a")[0].get("href")
                href = "http://books.toscrape.com/catalogue/" + href.replace("../", "")
                price = article.find("p", class_="price_color").text.strip()
                print(f"{title}|{category}|{price}|{href}")

                writer.writerow([title, category, price, href])
    print("===============================================================\n")