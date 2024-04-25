import sqlite3
import json

def insert_quotes(quotes, table_name, connection):
   
    insert_query = f"INSERT INTO {table_name} (quote, book_and_author) VALUES (?, ?)"
    cursor = connection.cursor()

    for quote in quotes:
        cursor.execute(insert_query, (quote["quote"], quote["book_and_author"]))

    connection.commit()
    cursor.close()


with open("quotes.json", "r") as f:
    quotes_data = json.load(f)
table_name = "book_quotes"
connection = sqlite3.connect("volume/gameguage.db")
insert_quotes(quotes_data, table_name, connection)
connection.close()
