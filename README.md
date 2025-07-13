# 📚 Book Scraping and Analysis Project

This project is a simple yet functional web scraping tool for collecting book information from the website [Books to Scrape](https://books.toscrape.com/), followed by data cleaning, filtering, and visualization using Python.

---

## 🔍 What this project does

- Scrapes book data (title, price, availability) from multiple pages of a sample e-commerce site (Books.toscrape.com)
- Cleans the price data (e.g., removes £ symbol, converts to numeric)
- Filters books based on price threshold
- Visualises:
  - Price distribution as a histogram
  - Availability as a bar chart

---

## 🛠️ Technologies Used

- `Python`
- `BeautifulSoup` – for parsing HTML
- `requests` – for HTTP requests
- `pandas` – for data manipulation
- `matplotlib` & `seaborn` – for data visualization

---

## 📂 Files

| File | Description |
|------|-------------|
| `multi_page_scraper.py` | Main script to scrape and process book data |
| `multi_page_output.csv` | Cleaned data of all books scraped |
| `filtered_output.csv` | Books priced at £20 or higher |
| `price_distribution.png` | Histogram of book prices |
| `availability_distribution.png` | Bar chart of book availability status |

---

## ▶️ How to run

1. Install required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas matplotlib seaborn
