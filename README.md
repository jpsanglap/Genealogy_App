# SALINLAHI: Filipino Genealogy CLI App

**SALINLAHI** is a simple command-line application that allows users to store, search, and delete basic family history data such as names, birthdates, and parents' names.

This project is intended as an entry-level portfolio project to demonstrate Python fundamentals such as:
- Object-Oriented Programming (OOP)
- File I/O using JSON
- Basic CLI interaction
- Simple data management

---

## Features

- ✅ Add a person's name, birthdate, and parents
- 🔍 Search for an existing person in the JSON file
- ❌ Delete a person’s information if found

---

## Getting Started

### Requirements

- Python 3.x

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/salinlahi.git
   cd salinlahi
Run the app:

bash
python main.py
File Structure
main.py - Entry point of the app

create_person.py - Handles creating, searching, saving, and deleting person data

familytree.py - Base class that stores common attributes

tree_image.py - Stores an ASCII art or intro image used in the CLI

family_data.json - Local storage file (created automatically after saving a person)

Future Plans
Add support for displaying family relationships (parents-children tree)

Improve data validation (dates, duplicate entries, etc.)

Add export options (e.g., CSV, visual family tree)

Optional GUI using Tkinter or web version with Flask

License
This project is open source and available under the MIT License.


