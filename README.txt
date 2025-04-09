# Book Scraper Project

This project scrapes book data from http://books.toscrape.com, analyzes it, and saves it as JSON.

## Features
- Scrapes title, price, availability, and description
- Saves structured data in JSON
- Calculates statistics (total books, average price)

## Setup
1. Clone the repo
2. Run: `pip install -r requirements.txt`
3. Execute: `python main.py`

## Future Improvements
- Add pagination
- Support CSV/XML export
- Use logging instead of print

## Limitations
- Currently scrapes only the first page
- No error retries for failed sub-pages

