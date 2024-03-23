import sqlite3

# Connect to the SQLite database (creates a new database file if it doesn't exist)
conn = sqlite3.connect('resumes.db')

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Create a table to store resumes information
cur.execute('''CREATE TABLE IF NOT EXISTS resumes (
               id INTEGER PRIMARY KEY,
               name TEXT,
               email TEXT,
               phone_number TEXT,
               previous_job_history TEXT,
               education TEXT,
               skills TEXT,
               resume_path TEXT)''')

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
