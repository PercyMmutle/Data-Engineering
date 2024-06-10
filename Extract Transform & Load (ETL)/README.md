# ETL Pipeline for Data Processing

## Overview
This Python script implements an ETL (Extract, Transform, Load) pipeline for processing data from various file formats (CSV, JSON, XML). The pipeline extracts raw data from files, transforms it by converting units of measurement, and loads the transformed data into a target CSV file. The code is designed to enhance data processing efficiency and facilitate the integration of AI tools for analysis.

## Features
- Extraction: Data is extracted from CSV, JSON, and XML files using specialized functions for each file format.
- Transformation: Raw data is transformed by converting inches to meters and pounds to kilograms.
- Logging: Progress of the ETL process is logged to a text file to track the execution and identify any issues.
- Versatile: Supports processing of diverse data sources and formats for flexibility in data analysis.

## Installation
1. Clone the repository to your local machine:

2. Navigate to the project directory:

3. Install the required Python libraries:

## Usage
1. Place your data files (CSV, JSON, XML) in the same directory as the script.
2. Run the script:

3. Monitor the progress and status of the ETL process through the log file.
4. Once completed, find the transformed data saved in the `transformed_data.csv` file.

## Dependencies
- Python 3.x
- pandas

## Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

