# SQLite3 Database Interaction with Pandas

## Overview
This Python script demonstrates how to interact with a SQLite3 database using pandas. It connects to an SQLite database, reads data from a CSV file into a pandas DataFrame, and then loads the DataFrame into the database as a table. It also performs various SQL queries on the database and demonstrates data appending to the table.

## Requirements
- Python 3.x
- pandas
- sqlite3

## Usage
1. Ensure you have Python installed on your system.
2. Install the required Python libraries using pip:
3. Clone the repository or download the script (`sqlite3_interaction.py`) to your local machine.
4. Ensure you have an SQLite database file (`STAFF.db`) in the same directory as the script.
5. Prepare a CSV file (`INSTRUCTOR.csv`) containing data to be loaded into the database table. Ensure the CSV file has columns corresponding to the table attributes defined in the script.
6. Update the `file_path` variable in the script to point to the location of your CSV file.
7. Run the script: python sqlite3_interaction.py

## Features
- Connects to SQLite3 database using `sqlite3` module.
- Reads CSV data into a pandas DataFrame.
- Loads DataFrame into SQLite database table using `to_sql()` method.
- Executes SQL queries on the database using pandas `read_sql()` method.
- Demonstrates appending data to the database table.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.