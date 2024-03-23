import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('resumes.db')
cur = conn.cursor()

# Execute a SELECT query to fetch data from the table
cur.execute('SELECT * FROM resumes')

# Fetch all rows from the result set
rows = cur.fetchall()

# Process the fetched rows
for row in rows:
    name = row[1]
    email = row[2]
    phone_number = row[3]
    previous_job_history = row[4]
    education = row[5]
    skills = row[6]
    resume_path = row[7]
    
    # Process the extracted data as needed
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone Number: {phone_number}")
    print(f"Previous Job History: {previous_job_history}")
    print(f"Education: {education}")
    print(f"Skills: {skills}")
    print(f"Resume Path: {resume_path}")
    print()

# Close the cursor and connection
cur.close()
conn.close()
