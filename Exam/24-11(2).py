from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.quotegarden.com/mind.html")
soup = BeautifulSoup(response.text, features = "html.parser")

text_1 = soup.find_all("p")

with open("text.txt", "w") as file:
    for text_2 in text_1:
        print (text_2.text)
        file.write(text_2.text)

