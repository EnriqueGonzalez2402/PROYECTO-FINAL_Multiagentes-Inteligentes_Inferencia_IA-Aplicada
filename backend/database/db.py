import sqlite3

DB_NAME = "database/aura.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn