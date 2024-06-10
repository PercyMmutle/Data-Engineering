# Code for ETL to Acquiring and Processing Information 
# from On the World Largest Banks

# Importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./etl_project_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n') 

    
def extract(url, table_attribs):
    """This function aims to extract the required information from the website and save it to a data frame.

    The function returns the data frame for further processing.
    """
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    table_body = soup.find_all('tbody')[0]

    table_rows = table_body.find_all('tr')
    data_frame = pd.DataFrame(columns=table_attribs)

    for row in table_rows:
        columns = row.find_all('td')

        if len(columns) != 0:
            anchor_tags = columns[1].find_all('a')

            # Check if the second column has multiple anchor tags.
            if len(anchor_tags) > 1:
                # Extract data from the anchor tag and the third column.
                anchor_tag = anchor_tags[1]

                if anchor_tag is not None:
                    data = {'Name': anchor_tag.contents[0].strip(),
                            'MC_USD_Billions': columns[2].contents[0].strip()}
                    temp_df = pd.DataFrame(data, index=[0])
                    data_frame = pd.concat([data_frame, temp_df], ignore_index=True)
                
        data_frame['MC_USD_Billions'] = data_frame['MC_USD_Billions'].str.replace(',', '').astype(float)
    # Return the DataFrame containing the extracted data.
    return data_frame

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    exchange_rate = pd.read_csv(csv_path)
    dict = exchange_rate.set_index('Currency').to_dict()['Rate']

    df['MC_GBP_Billion'] = [np.round(x * dict['GBP'], 2) for x in df['MC_USD_Billions']]
    df['MC_INR_Billion'] = [np.round(x * dict['INR'], 2) for x in df['MC_USD_Billions']]
    df['MC_EUR_Billion'] = [np.round(x * dict['EUR'], 2) for x in df['MC_USD_Billions']]

    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)


def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output) 

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''


url = 'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billions"]
db_name = 'Banks.db'
table_name = 'Largest_Banks'
output_path = './Largest_banks_data.csv'
csv_path = r'C:\Users\Percy\OneDrive\Desktop\Coursera\Data Engineering\GitHub\Data-Engineering\Extract Transform & Load (ETL)\ETL Project\exchange_rate.csv' # Change this path to access the file from your computer

log_progress('Preliminaries complete. Initiating ETL process')
df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df, csv_path)
log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, output_path)
log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect('World_Economies.db')
log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Running the query')

#Query 1
query_statement = f"SELECT * from {table_name}"
run_query(query_statement, sql_connection)
#Query 2
query_statement = f"SELECT AVG(MC_USD_Billions) from {table_name}"
run_query(query_statement, sql_connection)
#Query 3
query_statement = f"SELECT Name from {table_name}"
run_query(query_statement, sql_connection)


log_progress('Process Complete.')
sql_connection.close()