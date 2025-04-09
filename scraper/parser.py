import requests
from bs4 import BeautifulSoup
from models.data_models import Book, BookCollection
# import html
BASE_URL = "http://books.toscrape.com/"


def parse_data(html):
    soup = BeautifulSoup(html, "html.parser")
    book_collection = BookCollection()

    for book in soup.select(".product_pod"):
        title = book.h3.a["title"]

        # Remove any unwanted characters like 'Â' and then convert to float
        price_text = book.select_one(".price_color").text.strip()
        price = float(price_text.replace('£', '').replace('Â', '').strip())

        availability = book.select_one(".availability").text.strip()

        # Get the book's detail page link
        book_url = BASE_URL + book.h3.a["href"]
        # Fetch description from the book page
        description = get_book_details(book_url)

        # Create a Book instance and add it to the collection
        book = Book(
                title=title, price=price,
                availability=availability,
                description=description)
        book_collection.add_book(book)

    return book_collection


def get_book_details(book_url):
    response = requests.get(book_url)
    response.encoding = 'utf-8'  # Ensure the correct encoding
    soup = BeautifulSoup(response.text, "html.parser")

    description_elem = soup.select_one("#product_description ~ p")
    description = (
        description_elem.get_text(strip=True)
        if description_elem
        else "No description available"
    )

    availability_elem = soup.select_one(".instock.availability")
    availability = (
        availability_elem.text.strip()
        if availability_elem
        else "Not available"
    )

    return description, availability
