# import os
# import json
# import requests
# from bs4 import BeautifulSoup
# import re
from utils.file_handler import load_data

BASE_URL = "http://books.toscrape.com/"


# Function to analyze data from a JSON file
def analyze_data(file_path):
    try:
        # Load books data using load_data function
        books = load_data(file_path)

        if books is None:
            print("ERROR: No data to analyze.")
            return None

        num_books = len(books)  # Count the number of books
        avg_price = calculate_average_price(books)

        print(f"Average Price: ${avg_price:.2f}")
        print(f"Total Books: {num_books}")

        return {
            "total_books": num_books,
            "average_price": avg_price
        }
    except Exception as e:
        print(f"ERROR: Failed to analyze data -> {e}")
        return None


# Helper function to calculate the average price of books
def calculate_average_price(books):
    if not books:
        return 0.0
    total_price = sum(book.get("price", 0.0) for book in books)
    return total_price / len(books)  # Return the average price


# Now, call the analyze_data function to analyze the saved data
if __name__ == "__main__":
    analyze_data("data/output.json")
