import requests #access web pages on the internet
from bs4 import BeautifulSoup #analyse and extract certain info on the HTML
import pandas as pd #save data as csv

#specify base_url
url = "https://books.toscrape.com" 

res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

books = soup.select("article.product_pod")
data = []

for book in books:
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text
    availability = book.select_one(".availability").text.strip()
    data.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

#save as CSV
df = pd.DataFrame(data)
df.to_csv("single_page_output.csv", index=False, encoding="utf-8-sig")

print(f"{len(data)}books data has been scraped and saved to single_page_output.csv")