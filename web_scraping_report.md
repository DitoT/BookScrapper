
# Web Scraping Project Report

## The Website Chosen and Why

For this project, we selected [Books to Scrape](http://books.toscrape.com/) as our target website. This website is specifically designed for practicing web scraping and contains a large dataset of books, each with information such as title, price, availability, and a short description. It offers a structured layout, making it ideal for learning how to navigate HTML content using tools like BeautifulSoup and Requests.

Another advantage of using this website is that it simulates a real-world e-commerce platform without the legal and ethical concerns typically associated with scraping commercial websites. This allowed us to freely explore and extract data while focusing on technical implementation rather than access restrictions.

## Implementation Challenges and Solutions

### 1. HTML Parsing and Data Extraction
One of the initial challenges was understanding the HTML structure of the website. Each book entry is presented inside `<article>` tags, with details like the title embedded within `<h3>`, prices marked with a currency symbol, and availability hidden within CSS classes.

To solve this, we used **BeautifulSoup** to navigate the DOM tree, identify class names, and extract relevant data fields. We also used regular expressions to clean up price values and HTML entities.

### 2. Encoding Issues
When saving book descriptions in JSON format, we encountered issues where special characters (e.g., accented letters like `ô`, `é`) were being encoded as Unicode escape sequences (`\u00f4`, `\u00e9`). This made the output less readable.

We addressed this by ensuring all files were read and written with UTF-8 encoding. When saving JSON, we added the `ensure_ascii=False` parameter in the `json.dump` function, which preserved proper character display in the final file.

### 3. File and Folder Structure
Initially, we had issues with files not being saved because the `data/` folder didn’t exist. We added a check to automatically create the directory if it didn’t exist before saving the output file. This improved robustness and prevented the script from crashing due to missing folders.

### 4. Modularization
To meet the requirement for modular code, we split the project into clearly defined modules:
    - `models/` for data classes like `Book` and `BookCollection`
    - `scraper/` for collecting and parsing HTML
    - `utils/` for file operations and analysis
    - `main.py` for integrating everything together

This structure helped us keep the project organized and scalable.

## Analysis of the Collected Data

After successfully scraping the first page of the website, we collected 20 books, each with their respective title, price, availability, and description. This data was stored in a JSON file called `output.json`.

We then analyzed the dataset using the `analyze_data` function. The script calculated:
    - **Total number of books**: 20
    - **Average price**: approximately $38.05

From this small sample, we noticed that:
    - Most books were in stock and available for purchase.
    - Prices varied significantly, suggesting a diverse collection of book categories.
    - Some descriptions were missing, likely due to inconsistencies in the original HTML or placeholders.

This analysis provides a simple but useful summary of the dataset and could be expanded further with additional metrics like median price, most expensive book, or category distribution if we collected more data.

## Potential Improvements or Extensions

While the current implementation covers basic scraping and analysis, several enhancements could significantly improve the project:

    1. **Pagination Support**: The website has 50 pages. Currently, only the first page is scraped. Implementing pagination would allow us to collect data on all 1000 books.

    2. **Advanced Analysis**: We could include category-wise statistics, identify books with the highest or lowest prices, and analyze availability rates.

    3. **Export Formats**: Besides JSON, data could be exported to CSV or even a database (e.g., SQLite or PostgreSQL) for better querying and reporting.

    4. **Error Handling and Logging**: Adding structured logging instead of simple print statements would make the program more robust and easier to debug.

    5. **GUI or Web Interface**: A simple interface could allow users to scrape data, view statistics, and export results interactively.

    6. **Unit Testing**: Adding test cases for each module would improve code reliability and maintainability.

## Conclusion

This project gave us hands-on experience with real-world web scraping using Python. We learned how to navigate HTML documents, clean and structure data, and organize code modularly. It also helped us tackle common challenges such as character encoding, missing data, and file system errors. With further improvements, this project could serve as a foundation for more complex scraping and data analysis systems.
