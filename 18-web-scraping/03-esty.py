import requests
from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.etsy.com/c/jewelry"


driver = webdriver.Firefox()
driver.get(url)
html = driver.page_source

# response = requests.get(url)
soup = BeautifulSoup(html, "html.parser")


products = soup.find_all("li", class_="wt-list-unstyled")

for product in products:
    title = product.find("h2", class_="wt-text-truncate").text.strip()
    price = product.find("span", class_="currency-value").text.strip()
    link =  product.find("a", class_="listing-link")["href"]

    # # Fetch individual product page
    # product_response = requests.get(link)
    # product_soup = BeautifulSoup(product_response.content, "html.parser")

    # driver.get(link)
    # product_soup = driver.page_source

    # # Extract additional information
    # description = product_soup.find("h1", class_="wt-text-body-01 wt-line-height-tight wt-break-word wt-mt-xs-1").text.strip()
    # images = product_soup.find_all("img", class_="wt-max-width-full wt-horizontal-center wt-vertical-center carousel-image wt-rounded")

    # Print the extracted information
    print("Title:", title)
    print("Price:", price)
    print("Link:", link)
    # print("Description:", description)
    print("====================================================================================")
    # print("Images:")
    # for img in images:
    #     print(img["alt"] + ":", img.get('data-src'))
    # print()
