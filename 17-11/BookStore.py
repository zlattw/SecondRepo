from bs4 import BeautifulSoup
import requests

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, features = "html.parser")

books = soup.find_all("h3")
prices = soup.find_all("p", {"class": "price_color"})

with open("books.txt", "w") as file:
    for i in range(len(books)):
        book = books[i].a["title"]
        price = prices[i].text.strip()
        print(f"{book} {price}")
        file.write(f"{book} {price}\n")

