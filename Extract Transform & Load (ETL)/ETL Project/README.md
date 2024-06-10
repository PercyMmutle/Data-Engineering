# ETL Project: Acquiring and Processing Information from the World's Largest Banks
This Python script performs an ETL (Extract, Transform, Load) process to acquire information about the largest banks in the world from a Wikipedia page, transform the data, and load it into a CSV file and a SQLite database.

## Overview
The script extracts data from a Wikipedia page listing the largest banks globally, transforms the data to calculate market capitalization in different currencies, and loads the processed data into CSV and SQLite formats.

## Requirements
Python 3.x
BeautifulSoup (bs4)
pandas
numpy
sqlite3

## Instructions
**Extract:** The extract() function retrieves data from a Wikipedia page and returns it as a DataFrame.

**Transform:** The transform() function converts market capitalization from USD to GBP, INR, and EUR using exchange rates from a CSV file.

**Load to CSV:** The load_to_csv() function saves the transformed DataFrame to a CSV file.

**Load to Database:** The load_to_db() function stores the DataFrame in a SQLite database.

**Run Queries:** Several example queries are executed on the database to demonstrate data retrieval.

## How to Use
Ensure all required libraries are installed.
Update the url variable with the desired Wikipedia page URL.
Set the correct file paths for the CSV containing exchange rates (csv_path) and the output CSV file (output_path).
Run the script.

## Logging
The script logs each stage of the ETL process to a log file (etl_project_log.txt).

## Author
Developed by PercyMmutle

For more details, refer to the comments within the code.