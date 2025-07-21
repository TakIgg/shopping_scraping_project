import streamlit as st # for web dashboard
import sqlite3 # for database
import pandas as pd # for data analysis
import seaborn as sns # to customise data visualisation
import matplotlib.pyplot as plt # for data visualisaition

st.set_page_config(page_title="BookDashboard", layout="wide")
st.title("Book Data Dashboard")

# Connect to SQLite database
@st.cache_data  # Cache the connection
def load_data():
    conn = sqlite3.connect("books.db")
    df = pd.read_sql_query("SELECT * FROM books", conn)
    conn.close()
    return df

df = load_data()

# Data Overview
st.subheader("Data Preview")
st.write(df.head())

# Search Functionality (Filter Titles by keyword)
search_term = st.text_input("Search by Title")
if search_term:
    df = df[df["Title"].str.contains(search_term, case=False)]

# price demographic histogram
st.subheader("Price Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(df["Price"], bins=10, kde=True, color="skyblue", ax=ax1)
ax1.set_title("Book Price Distribution")
st.pyplot(fig1)

# Availability Status chart
st.subheader("Availability Status")
fig2, ax2 = plt.subplots()
sns.countplot(y="Availability",
              data=df,
              hue="Availability",
              palette="pastel",
              ax=ax2)
ax2.set_title("Availability")
st.pyplot(fig2)

# Statistics Summary
st.subheader("Price Statistics Summary")
st.write(df["Price"].describe())