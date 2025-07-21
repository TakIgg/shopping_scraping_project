# 📚 Book Scraper & Dashboard Project

This project demonstrates the complete workflow of web data extraction, data cleaning, local database storage, and interactive dashboard visualization using Python. The target website is [Books to Scrape](https://books.toscrape.com), a sandbox site designed for practicing scraping.

## 🔧 Technologies Used

- Python 3
- `requests` / `BeautifulSoup` – for web scraping
- `pandas` – for data cleaning and CSV output
- `sqlite3` – for local structured data storage
- `seaborn` / `matplotlib` – for data visualization
- `Streamlit` – for creating a lightweight interactive dashboard

## 🚀 Features

- Scrapes book data from multiple pages (titles, prices, availability)
- Cleans price fields and filters by price
- Saves data to both CSV and SQLite database
- Creates a histogram of book prices
- Visualizes availability status using a bar chart
- Adds a dummy record to simulate "Out of stock" data
- Interactive dashboard with:
  - Book title keyword search
  - Price distribution chart
  - Availability summary
  - Price statistics

## 💼 Why This Project Matters

This project simulates a real-world workflow where raw web data is extracted, structured, stored, and made accessible for non-technical users through a clean dashboard. 

Employers can evaluate:

- My ability to automate data collection
- My skills in data cleaning and preprocessing
- My familiarity with databases (SQLite) and data storage formats
- My capability to present data using interactive UI tools like Streamlit
- My overall understanding of end-to-end data pipeline design



---

To run the dashboard locally:

```bash
pip install streamlit pandas matplotlib seaborn
streamlit run dashboard.py

