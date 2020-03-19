import sqlite3

conn = sqlite3.connect('our_records.db')
print("Opened database successfully")

conn.execute('CREATE TABLE students_info (roll INTEGER PRIMARY KEY UNIQUE NOT NULL, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, country TEXT)')
print("Table created successfully")
conn.close()
