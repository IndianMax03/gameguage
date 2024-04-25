import sqlite3
import json
def insert_transformed_words(transformed_words, table_name, connection):
    """
    Args:
        transformed_words: Список словарей с полями "main_text" и "missed_text".
        table_name: Имя таблицы, в которую нужно вставить данные.
        connection: Подключение к базе данных SQLite.
    """
    insert_query = f"INSERT INTO {table_name} (main_text, missed_text) VALUES (?, ?)"

    cursor = connection.cursor()

    for word in transformed_words:
        try:
            cursor.execute(insert_query, (word["main_text"], word["missed_text"]))
        except sqlite3.IntegrityError:
            continue

    connection.commit()
    cursor.close()

with open("fill_words.json", "r") as f:

    transformed_data = json.load(f)

table_name = "gap_text"

connection = sqlite3.connect("volume/gameguage.db")
insert_transformed_words(transformed_data, table_name, connection)
connection.close()
