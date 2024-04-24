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
