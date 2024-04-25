import sqlite3
import json
def insert_words(words, table_name, connection):
    """
    Args:
        words: Список словарей с полем "word".
        table_name: Имя таблицы, в которую нужно вставить данные.
        connection: Подключение к базе данных SQLite.
    """
    insert_query = f"INSERT OR IGNORE INTO {table_name} (word) VALUES (?)"

    cursor = connection.cursor()

    for word in words:
        cursor.execute(insert_query, (word["word"],))

    connection.commit()
    cursor.close()



with open("words.json", "r") as f:
    data = json.load(f)

words = data
table_name = "en_words"

connection = sqlite3.connect("volume/gameguage.db")
insert_words(words, table_name, connection)
connection.close()