from bs4 import BeautifulSoup
import requests

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, features = "html.parser")

books = soup.find_all("h3")

with open("books.txt", "w") as file:
    for i in range(len(books)):
        book = books[i].a["title"]
        print(f"{book}")
        file.write(f"{book}\n")

