import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/chart/top"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

movies = soup.select("td.titleColumn")
ratings = soup.select("td.imdbRating strong")

with open("imdb.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Year", "Rating", "Link"])

    for movie, rating in zip(movies, ratings):
        title = movie.a.text
        year = movie.span.text
        rating_value = rating.text.strip()
        movie_url = "https://www.imdb.com" + movie.a["href"]

        print("Title:", title)
        print("Year:", year)
        print("Rating:", rating_value)
        print("Link:", movie_url)

        # Store the data in a CSV file
        writer.writerow([title, year, rating_value, movie_url])