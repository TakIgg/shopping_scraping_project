import requests #access web pages on the internet
from bs4 import BeautifulSoup #analyse and extract certain info on the HTML
import pandas as pd #convert data into dataframe(表形式) and save as csv
import matplotlib.pyplot as plt #data visualisation
import seaborn as sns   #for grapgh design

#specify base url                               #👇put {} to change page number
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

#create an array to store book data
all_data = []

#scrape 1~3pages
for page in range(1,4):
    # create the url of the current page
    url = base_url.format(page) #input the numbers in the range in rhe base_url
    print(f"Fetching: {url}")
    #Acquire the content of a web page
    res = requests.get(url)
    #Convert HTML into a readable format
    soup = BeautifulSoup(res.content, "html.parser")
    
    #Acquire all the item blocks on a page
    books = soup.select("article.product_pod")

    #Acquire each book information from the blocks
    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        availability = book.select_one(".availability").text.strip()
        #Input book details in "all_data" array
        all_data.append({
            "Title": title,
            "Price": price,
            "Availability": availability 
        })

# crate dateframe and Save as CSV
df = pd.DataFrame(all_data)

#11/Jul/25 Data Cleaning with str.replace, float()
#Remove "£" from Price array and change the data type into float
#for future filtering and analysis processes
df["Price"] = df["Price"].str.replace("£","",regex=False).astype(float)
df.to_csv("multi_page_output.csv", index=False, encoding="utf-8-sig")
print(f"{len(all_data)}books data has been scraped and saved in multi_page_output.csv")

#11/Jul/25 Filtering the data with pandas
#Extract items whose prices are more than 20 pounds
filtered_df = df[df["Price"]>= 20]

#save the extracted data as a new csv
filtered_df.to_csv("filtered_output.csv", index=False, encoding="utf-8-sig")

print(f"{len(filtered_df)}items are more than £20. Data has been saved as filtered_output.csv")

#11/Jul/25 Data visualisation with matplotlib, seaborn
#Graph Theme
sns.set(style="whitegrid")

#Price Demographic Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df["Price"], bins=10, kde=True, color="skyblue")
plt.title("Book Price Distribution")
plt.xlabel("Price(£)")
plt.ylabel("Number of Books")
plt.tight_layout()

#Save the graph
plt.savefig("price_histogram.png")
plt.close()
print("The Price Demographic Histogram chart was created and saved as price_histogram.png")

#In-Stock Bar Chart
#Check the availability of all the scraped items
print(df["Availability"].value_counts())

# dummy data that includes "Out of stock"
df.loc[len(df)] ={
    "Title": "Dummy Book",
    "Price": 9.99,
    "Availability": "Out of stock"
}
print("Dummy data included successfully!")
print(df["Availability"].value_counts())
plt.figure(figsize=(8,5))
sns.countplot(
    y="Availability",
    data=df,
    hue="Availability",
    palette="pastel",
    legend=False
    )
plt.title("Availability of Books")
plt.xlabel("count")
plt.ylabel("Availability")
plt.tight_layout()
plt.savefig("availability_distribution.png")
plt.close()
print("The In-stock Bar chart was created and saved as availability_distribution.png")