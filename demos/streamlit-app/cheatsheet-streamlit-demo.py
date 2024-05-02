# Import necessary libraries
import streamlit as st
import pandas as pd
import sqlite3

# Function to load data from CSV
def load_data(file):
    data = pd.read_csv(file)
    return data

# Function to create SQLite database and table
def create_db_table(data, db_name, table_name):
    conn = sqlite3.connect(db_name)
    data.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

# Function to read data from SQLite database
def read_data(db_name, table_name):
    conn = sqlite3.connect(db_name)
    data = pd.read_sql(f'SELECT * FROM {table_name}', conn)
    conn.close()
    return data

# Streamlit app
def main():
    st.title('ETL App')

    # Load data from CSV
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        st.write(data)

        # Create SQLite database and table
        db_name = st.text_input('Enter the name for your SQLite database:')
        table_name = st.text_input('Enter the name for your SQLite table:')
        if db_name and table_name:
            create_db_table(data, db_name, table_name)
            st.success('Database and table created successfully!')

            # Read data from SQLite database
            data_from_db = read_data(db_name, table_name)
            st.write(data_from_db)

if __name__ == '__main__':
    main()