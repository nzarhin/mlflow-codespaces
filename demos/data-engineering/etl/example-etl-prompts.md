# Example Prompts for ETL Python Notebook

1. Load Data from CSV

```text
Please load data from a csv file at location: ../../sample-data/data.csv
```

2. Create a SQLite (local database) with the same properties/headers as the CSV file

```text
Please create a sqlite db that will have a table in the database called some_data with the same column/property names as the CSV file.
```

3. Load and save the data from the CSV file to the SQLite database

```text
Please load and save all the data from the CSV file to the SQLite database.
```

4. Check/validate that the number of rows (line items) in the CSV file equals to the same number of records in the SQL Database (just soft to validate that the data transfer worked)

```text
Please check to see that the CSV file and the Database are similar by checking that the number of records in the CSV file is the same as the SQLite DB
```

5. In this step you will need to get your public IP address - you will need to add this address to the Azure SQL DB Firewall/Networking settings to allow connectivity to the Database

```text
Please write a python script to get my public ip address.
```
Now copy this IP address to Azure SQL Firewall settings.


6. Create to an Azure SQL DB based on the associated .env file, and create a table with the same properties as the SQLite DB

```text
Please create a connection to an Azure SQL DB using the .env file and create a table schema that mirrors/is simmilar to that of the SQLite DB
```

7. Copy and load the data in SQLite to Azure SQL

```
Please load all the data in SQLite and copy that data to the Azure SQL DB.
```

TODO:
- Add transform steps/example(s)

