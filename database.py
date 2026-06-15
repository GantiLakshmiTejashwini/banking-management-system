import sqlite3

conn = sqlite3.connect("bank.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    account_number TEXT PRIMARY KEY,
    name TEXT,
    balance REAL
)
""")

conn.commit()

print("Database Created Successfully")

conn.close()