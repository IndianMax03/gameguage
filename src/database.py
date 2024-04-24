import sqlite3

import logging

DB_NAME = "volume/gameguage.db"


def create_db(db_name: str = None) -> None:
    """Create the database if it does not exist."""
    global DB_NAME
    if db_name is not None and db_name != DB_NAME:
        logging.info("Replaced default database name %s with %s", DB_NAME, db_name)
        DB_NAME = db_name

    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()

        # ROWID as PK and a file name
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS speech (
                message TEXT NOT NULL
            )
            """
        )

        c.execute(
            """
            CREATE TABLE IF NOT EXISTS gap_text (
                main_text TEXT NOT NULL UNIQUE,
                missed_text TEXT NOT NULL
            )
            """
        )

        c.execute(
            """
            CREATE TABLE IF NOT EXISTS book_quotes (
                quote TEXT NOT NULL UNIQUE,
                book_and_author TEXT NOT NULL
            )
            """
        )

        conn.commit()
        c.close()


def get_random_speech() -> tuple[int, str]:
    """
    :return: (ROWID, message)
    """
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute(
            """
            SELECT ROWID, message FROM speech ORDER BY RANDOM() LIMIT 1
            """
        )
        speech = c.fetchone()
        c.close()
    return speech


def get_random_text_with_gap() -> tuple[str, str]:
    """
    :return: (main text, missed text)
    """
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute(
            """
            SELECT main_text, missed_text FROM gap_text ORDER BY RANDOM() LIMIT 1
            """
        )
        result = c.fetchone()
        c.close()
    return result


def get_random_book_quotes(number: int) -> list[tuple[str, str]]:
    """
    :return: list of (quote, book_and_author)
    """
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute(
            """
            SELECT quote, book_and_author FROM book_quotes ORDER BY RANDOM() LIMIT ?
            """,
            (number,),
        )
        result = c.fetchall()
        c.close()
    return result

