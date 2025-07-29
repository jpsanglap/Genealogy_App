# Salinlahi: A Filipino Genealogy App (CLI Version)

**Salinlahi** is a simple command-line interface (CLI) application written in Python for building a family history tree tailored for Filipino users. It allows you to input and manage basic genealogical data such as names, birthdates, and parents, and stores this data in a JSON file.

## Features

- Add a person's name, birthdate, and parent names
- Search for a person by first and/or last name
- Delete a person's record
- Save all entries in a JSON file
- Flexible birthdate entry: supports full date, month-year, year only, or unknown

## File Structure

- `main.py` – Entry point for the CLI application
- `create_person.py` – Handles creating, saving, deleting, and searching for a person
- `familytree.py` – Defines the FamilyTree class structure
- `tree_image.py` – Contains an ASCII image for app branding
- `family_data.json` – JSON file where all data is stored (created after first save)

## How to Run

1. Make sure you have Python 3 installed.
2. Clone or download this repository.
3. In your terminal or command prompt, run:

   ```bash
   python main.py
Follow the on-screen prompts to:

Add a new person

Search for an existing person

Delete a person

Date Entry Guidelines
Input format for birthdate:

Year only: YYYY

Month and year: MMM and YYYY

Complete date: DD, MMM, YYYY

Leave fields blank if unknown.

Example:

Year of birth (YYYY): 1980
Month of birth (MMM): Aug
Day of birth (DD): (leave blank)
This will be saved as: Aug-1980

Sample Data Format

{
  "firstname": "Juan",
  "lastname": "Dela Cruz",
  "birthdate": "1980",
  "parents": {
    "father": "Pedro Dela Cruz",
    "mother": "Maria Santos"
  }
}
Future Plans
Convert this app to a Flask-based web application

Use a database (like SQLite or PostgreSQL) instead of JSON

Add visual family tree generation

Author
David John Paul Sanglap
Filipino Genealogist | Software Developer
📚 Author of Ninuno: Searching Your Filipino Ancestors

