# Resume Parser : Fast Paced Recruiting

## Set-Up :
[Github Repository](https://github.com/spacecowbye/resume_parser) for the entire codebase till my part, uploading resumes via a google drive folder.


# Resume Parser Setup Guide

This guide will help you set up and run the resume parser project from the provided GitHub repository.

## 1)  Clone the Repository

First, you need to clone the repository to your local machine. Open your terminal and execute the following command:

```
git clone https://github.com/spacecowbye/resume_parser.git
```

## 2) Navigate into the project directory:

```
cd resume_parser
```

## 3) Set up the virtual environment

```
python3 -m venv venv
```
## 4) Activate the virtual environment

```
source venv/bin/activate
```

## 5) Install the requirements

```
pip install -r requirements.txt
```

## 6) Run the app 

```
python3 app.py
```
# Once the app has run, this means your model has been setup and can execute on a single resume, now to parse all resumes from a google drive folder you can follow the following steps.

# Resume Processing with Google Drive and OpenAI

This document describes how to set up and run a Python script to download resumes from Google Drive, process them using OpenAI and Parcv, and store the extracted information in an SQLite database.

## Prerequisites

1. **Python 3.x** installed on your machine.
2. **Google Cloud Platform** account.
3. **OpenAI API Key**.

## Setting Up Google Cloud Project

1. **Create a Project in Google Cloud Console**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Click on the project dropdown (top-left) and select "New Project".
   - Enter a project name and click "Create".

2. **Enable Google Drive API**:
   - With your project selected, go to the [Google Drive API page](https://console.cloud.google.com/apis/library/drive.googleapis.com).
   - Click "Enable".

3. **Create OAuth 2.0 Credentials**:
   - Go to the [Credentials page](https://console.cloud.google.com/apis/credentials).
   - Click "Create Credentials" and select "OAuth 2.0 Client ID".
   - Configure the consent screen if prompted:
     - Set up OAuth consent screen by providing required details like application name, support email, etc.
     - Save and continue.
   - Choose "Application type" as "Desktop app" and provide a name.
   - Click "Create".
   - Download the credentials JSON file and save it as `credentials.json`.

## Installing Required Python Packages

Make sure you have the necessary Python packages installed:

```sh
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client openai

```
## Run the following  python scripts  
```
python3 db.py
python3  main.py (You will need an openai api key for this)
```
## Paste the link in the terminal

## Run extract_from_db.py to get the extracted information from the databse





