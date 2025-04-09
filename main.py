from scraper.collector import collect_data
from scraper.parser import parse_data
from utils.file_handler import save_data
from BookScrapper.utils.analyzer import analyze_data

URL = "http://books.toscrape.com/"


def main():
    raw_html = collect_data(URL)
    if raw_html:
        # Get the BookCollection object from parse_data()
        book_collection = parse_data(raw_html)

        # Convert BookCollection to a list of dictionaries
        #  For JSON serialization
        books_dict = [book.to_dict() for book in book_collection.books]

        # Save the books to a JSON file
        save_data(books_dict, "data/output.json")

        # Perform analysis
        analysis = analyze_data("data/output.json")
        print("Analysis Result:", analysis)
    else:
        print("Failed to collect data.")


if __name__ == "__main__":
    main()
