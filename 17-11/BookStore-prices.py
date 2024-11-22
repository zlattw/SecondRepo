from bs4 import BeautifulSoup
import requests

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, features = "html.parser")

prices = soup.find_all("p", class_="price_color")

with open("price.txt", "w", encoding="utf-8") as file:
    for i in range(len(prices)):
        price = prices[i]
        print(price.text)
        file.write(price.text + "\n")