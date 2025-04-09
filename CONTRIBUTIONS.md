Dimitri Tutberidze:

1) Organized code into modules:
        Created the folder structure (models/, scraper/, utils/)
        Added __init__.py files for module packaging

2) Created models:
        Implemented Book and BookCollection classes with validation logic
        
3) Developed file operations:
        Built save_data and load_data functions in file_handler.py

4) Added code comments and docstrings

5) Handled JSON encoding/decoding issues (e.g., utf-8)

Elene Zurabiani:

1) Implemented scraping logic:

        Developed collect_data in collector.py
        Built parse_books function in parser.py using BeautifulSoup

2) Developed analyzer logic:

        Built analyze_data and calculate_average_price

3) Wrote the README.md with setup, structure, and usage

4) Created requirements.txt

5) Documented limitations and suggestions for improvements