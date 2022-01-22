import requests
from bs4 import BeautifulSoup

# requesting data from both pages:
response1 = requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")
imdb_html = response1.text

response2 = requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt")
imdb_html2 = response2.text

# scrapping from separate pages
soup1 = BeautifulSoup(imdb_html, "html.parser")
soup2 = BeautifulSoup(imdb_html2, "html.parser")

# create two lists from separate pages:
all_movie1 = soup1.find_all(name="h3", class_="lister-item-header")
all_movies2 = soup1.find_all(name="h3", class_="lister-item-header")

# list of both pages:
all_movies = all_movies1 + all_movies2

rank = 1
for movie in all_movies:
    m = movie.a.string
    row = f"{rank} {m}\n"
    # making text file with a list:
    with open("top_100_movies.txt", mode="a") as file:
        file.write(row)
    rank += 1
