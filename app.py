import os
import json
import re
import sqlite3
from parcv import parcv
from openai import OpenAI
from src.openai_query import *
from src.resume_prompts import *


conn = sqlite3.connect('resumes.db')
cur = conn.cursor()
# Create a table to store resumes information if it doesn't exist
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

# Initialize OpenAI client
#api_key = ""
openai_client = OpenAI(api_key=api_key)

# Initialize the parser
parser = parcv.Parser(pickle=True, load_pickled=True)

# Specify the folder path containing the resumes
folder_path = '/Users/vatsal/Desktop/Hackathons/Mined-Hackathon/ResumeParser/resumes_pdf'

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf') :
        # Construct the full path to the resume file
        resume_path = os.path.join(folder_path, filename)

        # Parse the resume
        json_output = parser.parse(resume_path)

        # Get resume lines and segments
        lines = parser.get_resume_lines()
        resume_text = '\n'.join(lines)
        segments = parser.get_resume_segments()

        # Load and modify the output JSON for better efficiency
        with open("output.json", "r") as json_file:
            resume_data = json.load(json_file)
            work_exp_string = ""
            if any(entry.get("Start Date") == "" for entry in resume_data.get("Job History", [])):
                # Query work experience if start date is empty for any job entry
                work_exp_resume = get_answer_openai(openai_client, get_work_experience_resume(resume_text))
                resume_data["Job History"] = work_exp_resume
                work_exp_string = re.sub(r'[\[\]{}]', '', work_exp_resume)
            else:
                job_history_text = ""
                for entry in resume_data["Job History"]:
                    job_title = entry["Job Title"]
                    company = entry["Company"]
                    start_date = entry["Start Date"]
                    end_date = entry["End Date"]
                    job_entry_text = f"Job Title: {job_title}\nCompany: {company}\nStart Date: {start_date}\nEnd Date: {end_date}\n\n"
                    job_history_text += job_entry_text
                work_exp_string = job_history_text

            education_string = ""
            for entry in resume_data["Education"]:
                education_string += f"Studied {entry['Field of Study']} at {entry['School Name']} with qualification {entry['Qualification']}\n"
            skills_resume = resume_data["Skills"]
            skills_string = ''
            if not skills_resume:
                skills_resume = get_answer_openai(openai_client, get_skills_resume(resume_text)).split(':')[-1].strip()
                skills_string = skills_resume
            else:
                skills_string = ",".join(resume_data["Skills"])
            skills_string = f"Skills extracted from resume are : {skills_string}"
            name_string = resume_data["Name"]
            email_string = resume_data["Contact Info"]["Email"]
            phone_number_string = resume_data["Contact Info"]["phone1"]

        # Insert the resume information into the database
        cur.execute('''INSERT INTO resumes (name, email, phone_number, previous_job_history, education, skills, resume_path)
                       VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (name_string, email_string, phone_number_string, work_exp_string, education_string,
                     skills_string, resume_path))

        # Commit the transaction
        conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

