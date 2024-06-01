from parcv import parcv
import re
import json


parser = parcv.Parser(pickle=True, load_pickled=True)


# GIVE ABSOLUTE PATH TO THE RESUME HERE
########################
resume_path = '/Users/vatsal/Desktop/orangewood/resume_parser/resume_pratyush.pdf'
########################

json_output = parser.parse(resume_path)
print(json_output)

lines = parser.get_resume_lines()
print(lines)

segments = parser.get_resume_segments()
print(segments)

file_name = "output.json"

parser.save_as_json(file_name)
 
