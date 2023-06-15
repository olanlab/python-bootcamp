import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

movies = soup.select("td.titleColumn")
ratings = soup.select("td.imdbRating strong")

for movie, rating in zip(movies, ratings):
    title = movie.a.text
    year = movie.span.text
    rating_value = rating.text.strip()
    movie_url = "https://www.imdb.com" + movie.a["href"]

    print("Title:", title)
    print("Year:", year)
    print("Rating:", rating_value)
    print("Link:", movie_url)