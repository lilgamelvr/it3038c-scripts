from bs4 import BeautifulSoup
import re
import requests

url = "http://quotes.toscrape.com"
response = requests.get(url)

if response.status_code == 200:
    html = response.text

soup = BeautifulSoup(html, "html.parser")

for quote in soup.find_all("span", class_="text"):
    text = quote.get_text()
    author = quote.find_next("small", class_="author").get_text()
    tag = quote.find_next("a", class_="tag").get_text()
    print(f"Quote: {text}\nAuthor: {author}\nTop Tag: {tag}\n")
