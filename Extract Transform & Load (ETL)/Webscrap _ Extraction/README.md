# Film Ranking Web Scraper

## Overview
This Python script scrapes data from a webpage containing a list of the 100 most highly-ranked films. It extracts information such as the film's average rank, title, and release year, and stores it in both a CSV file and a SQLite database for further analysis or integration with other applications. The script utilizes the requests library to fetch the webpage, BeautifulSoup for parsing HTML content, and pandas for data manipulation and storage.

## Usage
1. Ensure you have Python installed on your system.
2. Install the required Python libraries using pip:
3. Clone the repository or download the script (`film_ranking_scraper.py`) to your local machine.
4. Run the script:
5. Monitor the script's execution to see the scraped data printed to the console.
6. Find the extracted data saved in a CSV file named `top_50_films.csv`.
7. Access the SQLite database (`Movies.db`) to view the scraped data stored in the `Top_50` table.

## Dependencies
- Python 3.x
- requests
- beautifulsoup4
- pandas

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository, make changes, and submit a pull request.
